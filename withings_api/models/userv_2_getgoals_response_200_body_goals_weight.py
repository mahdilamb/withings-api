from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Userv2GetgoalsResponse200BodyGoalsWeight")


@_attrs_define
class Userv2GetgoalsResponse200BodyGoalsWeight:
    """Weight.

    Attributes:
        unit (Union[Unset, int]): Power of ten to multiply the ```value``` field to get the real value.<br>Formula:
            ```value * 10^unit = real value```.<br>Eg: ```value = 20 and unit = -1 => real value = 2```. Example: -3.
        value (Union[Unset, int]): Value for the measure in S.I. units (kilograms, meters etc...). Value should be
            multiplied by 10 to the power of ```units``` to get the real value. Example: 70500.
    """

    unit: Union[Unset, int] = UNSET
    value: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit = self.unit

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit is not UNSET:
            field_dict["unit"] = unit
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        unit = d.pop("unit", UNSET)

        value = d.pop("value", UNSET)

        userv_2_getgoals_response_200_body_goals_weight = cls(
            unit=unit,
            value=value,
        )

        userv_2_getgoals_response_200_body_goals_weight.additional_properties = d
        return userv_2_getgoals_response_200_body_goals_weight

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
