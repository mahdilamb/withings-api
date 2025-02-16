from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeartMeasurementObjectBloodpressure")


@_attrs_define
class HeartMeasurementObjectBloodpressure:
    """
    Attributes:
        diastole (Union[Unset, int]): Diastole value. Example: 100.
        systole (Union[Unset, int]): Systole value. Example: 101.
    """

    diastole: Union[Unset, int] = UNSET
    systole: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        diastole = self.diastole

        systole = self.systole

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if diastole is not UNSET:
            field_dict["diastole"] = diastole
        if systole is not UNSET:
            field_dict["systole"] = systole

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        diastole = d.pop("diastole", UNSET)

        systole = d.pop("systole", UNSET)

        heart_measurement_object_bloodpressure = cls(
            diastole=diastole,
            systole=systole,
        )

        heart_measurement_object_bloodpressure.additional_properties = d
        return heart_measurement_object_bloodpressure

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
