from copy import deepcopy
import os
import re
import shutil
import tempfile
from types import MappingProxyType
from typing import (
    Any,
    Callable,
    Sequence,
    TypeAlias,
    TypeGuard,
    Generator,
)
import typing

import yaml
from openapi_python_client.schema import OpenAPI
from typer.testing import CliRunner
from openapi_python_client.cli import app as openapi_python_client_app

DictLocation: TypeAlias = tuple[str | int, ...]


def create_fixer_mappings() -> dict[
    DictLocation, Callable[[DictLocation, Any, dict[str, Any]], None]
]:
    @typing.no_type_check
    def get_element(loc: DictLocation, data: dict[str, Any]) -> Any:
        el = data
        for k in loc:
            el = el[k]
        return el

    def string_to_mac_address(el: dict[str, Any]):
        el["type"] = "string"
        el["pattern"] = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
        el["format"] = "macaddress"

    def fix_path_schema(loc: DictLocation, val: Any, data: dict[str, Any]):
        el = get_element(loc[:-2], data)
        if val == "list of integers":
            el["schema"]["type"] = "string"
            el["schema"]["pattern"] = r"(\d+,)+\d+"
        elif val == "macaddress":
            string_to_mac_address(el["schema"])
        elif val in ("rawint", "id16", "id32m64", "id64n", "id64", "id32"):
            el["schema"]["type"] = "integer"
            el["schema"]["format"] = val
        elif val in (
            "json_array",
            "json",
            "timezone",
            "email",
            "json_string",
            "array of strings",
            "array of integers",
            "array of object",
            "array of integer",
            "partner_redirect_uri",
        ):
            el["schema"]["type"] = "string"
            el["schema"]["format"] = val
        elif val == "pgboolean":
            el["schema"]["type"] = "string"
            el["schema"]["enum"] = ["t", "f"]

    def fix_path_nested_schema(loc: DictLocation, val: Any, data: dict[str, Any]):
        el = get_element(loc[:-1], data)
        match val:
            case "array of integers":
                el["type"] = "array"
                el["items"] = {"type": "integer"}
            case "array of strings":
                el["type"] = "array"
                el["items"] = {"type": "string"}
            case _:
                ...

    def fix_empty_properties(loc: DictLocation, val: Any, data: dict[str, Any]):
        if len(loc) != 11:
            return
        el = get_element(loc[:10], data)
        if el.get("properties") == []:
            del el["properties"]
            el["additionalProperties"] = True

    def fix_component_schema(loc: DictLocation, val: Any, data: dict[str, Any]):
        el = get_element(loc[:-1], data)
        if not is_dict(el):
            return
        if val == "macaddress":
            return string_to_mac_address(el)
        if val == "array" and "items" not in el:
            el["items"] = {
                "anyOf": [
                    {"type": "string"},
                    {"type": "object", "additionalProperties": True},
                ]
            }
            return
        if " " in val:
            match val:
                case "array of integers":
                    el["type"] = "array"
                    el["items"] = {"type": "integer"}
                case "array of strings":
                    el["type"] = "array"
                    el["items"] = {"type": "string"}
                case _:
                    ...

    def fix_component_examples(loc: DictLocation, val: Any, data: dict[str, Any]):
        if is_list_or_tuple(val):
            el = get_element(loc[:-2], data)
            el["examples"] = [val]
            return
        el = get_element(loc[:-1], data)
        if is_dict(el):
            el["examples"] = [el.pop("example")]

    return {
        ("paths", "*", "*", "*", "*", "schema", "type"): fix_path_schema,
        (
            "paths",
            "*",
            "*",
            "responses",
            "*",
            "content",
            "application/json",
            "schema",
            "properties",
            "*",
            "properties",
            "*",
            "properties",
            "*",
            "type",
        ): fix_path_nested_schema,
        ("components", "schemas", "*", "properties", "*", "type"): fix_component_schema,
        (
            "components",
            "schemas",
            "*",
            "properties",
            "*",
            "items",
            "type",
        ): fix_component_schema,
        (
            "paths",
            "*",
            "*",
            "responses",
            "*",
            "content",
            "application/json",
            "schema",
            "properties",
            "*",
        ): fix_empty_properties,
        (
            "components",
            "schemas",
            "*",
            "properties",
            "*",
            "example",
        ): fix_component_examples,
    }


FIXERS = MappingProxyType(create_fixer_mappings())


def is_dict(val: object) -> TypeGuard[dict[str, Any]]:
    """TypeGuard for dictionary."""
    return isinstance(val, dict)


def is_list_or_tuple(val: object) -> TypeGuard[Sequence[Any]]:
    """TypeGuard for list or tuple."""
    return isinstance(val, (list, tuple))


@typing.no_type_check
def dict_generator(
    data: dict[str, dict[str, Any] | Sequence[Any] | Any],
    loc: DictLocation = (),
) -> Generator[tuple[DictLocation, Any], None, None]:
    """Traverse through a dictionary."""
    if is_dict(data):
        for key, value in data.items():
            if is_dict(value):
                yield from dict_generator(value, loc + (key,))
            elif is_list_or_tuple(value):
                for i, element in enumerate(value):
                    yield from dict_generator(element, loc + (key, i))
            else:
                yield loc + (key,), value
    else:
        yield loc, data


def fix_schema(data: dict[str, Any]):
    def matches(query: DictLocation, location: DictLocation) -> bool:
        if len(query) > len(location):
            return False
        return all(q in ("*", loc) for loc, q in zip(location, query))

    result = deepcopy(data)
    result["openapi"] = "3.1.0"
    for location, value in dict_generator(data):
        for fn in (
            fixer for query, fixer in FIXERS.items() if matches(query, location)
        ):
            fn(location, value, result)
    return result


def extract_path(data: dict[str, Any], path: str):
    data = deepcopy(data)
    data["paths"] = {path.strip(): data["paths"][path]}
    OpenAPI.model_validate(data)
    runner = CliRunner()
    with (
        tempfile.TemporaryDirectory() as out_dir,
        tempfile.NamedTemporaryFile("w", suffix=".yaml") as fp,
    ):
        yaml.dump(data, fp)
        result = runner.invoke(
            openapi_python_client_app,
            ["generate", "--path", fp.name, "--output-path", out_dir, "--overwrite"],
        )

        shutil.copytree(
            os.path.join(out_dir, "withings_developer_documentation_client", "api"),
            "withings_api/api",
            dirs_exist_ok=True,
        )
        shutil.rmtree(
            os.path.join(out_dir, "withings_developer_documentation_client", "api")
        )

        shutil.copytree(
            os.path.join(out_dir, "withings_developer_documentation_client"),
            "withings_api",
            dirs_exist_ok=True,
        )
    if result.exit_code != 0:
        raise Exception(result.stdout)
    return result


def main():
    version = "0.1.0"
    if os.path.exists(init_path := "withings_api/__init__.py"):
        with open(init_path, "r") as fp:
            version = next(
                re.finditer(r"""^__version__\s*=\s*['"]([^'"]*)"\s$""", fp.read(), re.M)
            ).group(1)
    with open("schemas/openapi-2.0.raw.yaml") as fp:
        data = yaml.load(fp, Loader=yaml.FullLoader)
        data.pop("x-tagGroups", None)
        data.pop("tags", None)
        data["paths"] = {
            path[len("https://wbsapi.withings.net") :]: details
            for path, details in data["paths"].items()
            if path.startswith("https://wbsapi.withings.net/")
        }
        data = fix_schema(data)
        for path in data["paths"]:
            extract_path(data, path)
        with open(init_path, "a") as fp:
            fp.writelines(["", f'__version__ = "{version}"'])


if __name__ == "__main__":
    main()
