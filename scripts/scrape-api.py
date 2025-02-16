"""Scrape Withings redocly documentation to get an OpenAPI schema.

Note: this requires node to be installed.
"""

import yaml
import json
import os
import re
import subprocess
import tempfile
from typing import Any, Generator
import requests
import tree_sitter
import tree_sitter_javascript as tsjavascript


REDOCLY_PATH = "https://oauth.withings.com/api-reference"
JS_SCRIPT_SRC_PATTERN = re.compile(
    r"<script\s+.*?src=['\"]([^'\"]*?)['\"]", re.MULTILINE | re.DOTALL
)


def get_api():
    def extract_spec_raw(js: str):
        def traverse_tree(
            tree: tree_sitter.Tree,
        ) -> Generator[tree_sitter.Node, None, None]:
            cursor = tree.walk()

            visited_children = False
            while True:
                if not visited_children:
                    node = cursor.node
                    if node is not None:
                        yield node
                    if not cursor.goto_first_child():
                        visited_children = True
                elif cursor.goto_next_sibling():
                    visited_children = False
                elif not cursor.goto_parent():
                    break

        parser = tree_sitter.Parser(tree_sitter.Language(tsjavascript.language()))
        tree = parser.parse(js.encode())
        text = None
        for el in traverse_tree(tree):
            if el.text:
                _text = el.text.decode()
                if _text.find("apiSpec") > 0:
                    text = _text
        if text is None:
            raise RuntimeError("Could not find spec")
        return (
            text.rstrip()
            .rstrip(";")
            .replace("required: !0", "required: true,")
            .replace("required: !1", "required: false,")
        )

    def convert_to_json(spec: str) -> dict[str, Any]:
        with (
            tempfile.TemporaryDirectory() as tmpdir,
            open(os.path.join(tmpdir, "input.js"), "w") as input_file,
            open(os.path.join(tmpdir, "output.json"), "a+") as output_file,
        ):
            input_file.write("export const r=" + spec)
            subprocess.run(
                rf"""node -e 'import {{writeFileSync}} from "node:fs";import {{ r }} from "{tmpdir}/input.js";writeFileSync("{output_file.name}", JSON.stringify(r));'""",
                shell=True,
            )
            return json.load(output_file)["apiSpec"]

    redocly = requests.get(REDOCLY_PATH)
    js_assets = re.findall(JS_SCRIPT_SRC_PATTERN, redocly.text)
    main_js_url = next(asset for asset in js_assets if "/main" in asset)
    main_js = requests.get(REDOCLY_PATH.rsplit("/", 1)[0] + main_js_url).text
    spec = extract_spec_raw(main_js)
    spec_json = convert_to_json(spec)
    return spec_json


def main():
    api = get_api()
    with open(
        os.path.join("schemas", f"openapi-{api['info']['version']}.raw.yaml"), "w"
    ) as fp:
        yaml.dump(api, fp, indent=2, sort_keys=False)


if __name__ == "__main__":
    main()
