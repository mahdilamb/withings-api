from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeasureObject")


@_attrs_define
class MeasureObject:
    """
    Attributes:
        algo (Union[Unset, int]): Deprecated.
        fm (Union[Unset, int]): Deprecated.
        position (Union[Unset, int]): The device's position during the measure.


            | Value | Description|
            |---|---|
            |0 | Right Wrist|
            |1 | Left Wrist|
            |2 | Right Arm|
            |3 | Left Arm|
            |4 | Right Foot|
            |5 | Left Foot|
            |6 | Between Legs|
            |8 | Left part of the body|
            |9 | Right part of the body|
            |10 | Left leg|
            |11 | Right leg|
            |12 | Torso|
            |13 | Left hand|
            |14 | Right hand|
        type_ (Union[Unset, int]): Type of the measure. See ```meastype``` input parameter.
        unit (Union[Unset, int]): Power of ten to multiply the ```value``` field to get the real value.<br>Formula:
            ```value * 10^unit = real value```.<br>Eg: ```value = 20 and unit = -1 => real value = 2```.
        value (Union[Unset, int]): Value for the measure in S.I. units (kilograms, meters etc...). Value should be
            multiplied by 10 to the power of ```units``` to get the real value.
    """

    algo: Union[Unset, int] = UNSET
    fm: Union[Unset, int] = UNSET
    position: Union[Unset, int] = UNSET
    type_: Union[Unset, int] = UNSET
    unit: Union[Unset, int] = UNSET
    value: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        algo = self.algo

        fm = self.fm

        position = self.position

        type_ = self.type_

        unit = self.unit

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if algo is not UNSET:
            field_dict["algo"] = algo
        if fm is not UNSET:
            field_dict["fm"] = fm
        if position is not UNSET:
            field_dict["position"] = position
        if type_ is not UNSET:
            field_dict["type"] = type_
        if unit is not UNSET:
            field_dict["unit"] = unit
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        algo = d.pop("algo", UNSET)

        fm = d.pop("fm", UNSET)

        position = d.pop("position", UNSET)

        type_ = d.pop("type", UNSET)

        unit = d.pop("unit", UNSET)

        value = d.pop("value", UNSET)

        measure_object = cls(
            algo=algo,
            fm=fm,
            position=position,
            type_=type_,
            unit=unit,
            value=value,
        )

        measure_object.additional_properties = d
        return measure_object

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
