from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeartMeasurementObjectEcg")


@_attrs_define
class HeartMeasurementObjectEcg:
    """
    Attributes:
        afib (Union[Unset, int]): Atrial fibrillation classification.


            | Value | Description|
            |---|---|
            |0 | Negative|
            |1 | Positive|
            |2 | Inconclusive|
             Example: 1.
        signalid (Union[Unset, int]): Id of the signal. Example: 48.
    """

    afib: Union[Unset, int] = UNSET
    signalid: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        afib = self.afib

        signalid = self.signalid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if afib is not UNSET:
            field_dict["afib"] = afib
        if signalid is not UNSET:
            field_dict["signalid"] = signalid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        afib = d.pop("afib", UNSET)

        signalid = d.pop("signalid", UNSET)

        heart_measurement_object_ecg = cls(
            afib=afib,
            signalid=signalid,
        )

        heart_measurement_object_ecg.additional_properties = d
        return heart_measurement_object_ecg

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
