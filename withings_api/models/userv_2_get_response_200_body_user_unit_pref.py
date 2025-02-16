from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Userv2GetResponse200BodyUserUnitPref")


@_attrs_define
class Userv2GetResponse200BodyUserUnitPref:
    """User's unit preferences (cf. [Unit preferences](#tag/models/Unit-preferences) model).

    Attributes:
        distance (Union[Unset, int]):  Example: 6.
        height (Union[Unset, int]):  Example: 6.
        temperature (Union[Unset, int]):  Example: 11.
        weight (Union[Unset, int]):  Example: 1.
    """

    distance: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    temperature: Union[Unset, int] = UNSET
    weight: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        distance = self.distance

        height = self.height

        temperature = self.temperature

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distance is not UNSET:
            field_dict["distance"] = distance
        if height is not UNSET:
            field_dict["height"] = height
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        distance = d.pop("distance", UNSET)

        height = d.pop("height", UNSET)

        temperature = d.pop("temperature", UNSET)

        weight = d.pop("weight", UNSET)

        userv_2_get_response_200_body_user_unit_pref = cls(
            distance=distance,
            height=height,
            temperature=temperature,
            weight=weight,
        )

        userv_2_get_response_200_body_user_unit_pref.additional_properties = d
        return userv_2_get_response_200_body_user_unit_pref

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
