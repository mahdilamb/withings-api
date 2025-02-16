from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Userv2AddtorpmResponse200BodyProgram")


@_attrs_define
class Userv2AddtorpmResponse200BodyProgram:
    """
    Attributes:
        cohortid (Union[Unset, int]):  Example: 18035.
        id (Union[Unset, int]):  Example: 50.
        name (Union[Unset, str]):  Example: Glucose Care Team.
        timezone (Union[Unset, str]): Timezone for the date. Example: Europe/Paris.
    """

    cohortid: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cohortid = self.cohortid

        id = self.id

        name = self.name

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cohortid is not UNSET:
            field_dict["cohortid"] = cohortid
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        cohortid = d.pop("cohortid", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        timezone = d.pop("timezone", UNSET)

        userv_2_addtorpm_response_200_body_program = cls(
            cohortid=cohortid,
            id=id,
            name=name,
            timezone=timezone,
        )

        userv_2_addtorpm_response_200_body_program.additional_properties = d
        return userv_2_addtorpm_response_200_body_program

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
