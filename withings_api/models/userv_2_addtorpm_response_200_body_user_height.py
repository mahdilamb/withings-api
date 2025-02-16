from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Userv2AddtorpmResponse200BodyUserHeight")


@_attrs_define
class Userv2AddtorpmResponse200BodyUserHeight:
    """
    Attributes:
        type_measure (Union[Unset, int]):  Example: 4.
        unit_measure (Union[Unset, int]):  Example: -2.
        value_measure (Union[Unset, int]):  Example: 180.
    """

    type_measure: Union[Unset, int] = UNSET
    unit_measure: Union[Unset, int] = UNSET
    value_measure: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_measure = self.type_measure

        unit_measure = self.unit_measure

        value_measure = self.value_measure

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_measure is not UNSET:
            field_dict["type_measure"] = type_measure
        if unit_measure is not UNSET:
            field_dict["unit_measure"] = unit_measure
        if value_measure is not UNSET:
            field_dict["value_measure"] = value_measure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_measure = d.pop("type_measure", UNSET)

        unit_measure = d.pop("unit_measure", UNSET)

        value_measure = d.pop("value_measure", UNSET)

        userv_2_addtorpm_response_200_body_user_height = cls(
            type_measure=type_measure,
            unit_measure=unit_measure,
            value_measure=value_measure,
        )

        userv_2_addtorpm_response_200_body_user_height.additional_properties = d
        return userv_2_addtorpm_response_200_body_user_height

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
