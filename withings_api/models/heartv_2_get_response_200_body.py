from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Heartv2GetResponse200Body")


@_attrs_define
class Heartv2GetResponse200Body:
    """Response data.

    Attributes:
        sampling_frequency (Union[Unset, int]): Signal Sampling Frequency (Hz). Example: 500.
        signal (Union[Unset, list[int]]): Signal value in micro-volt (μV). Example: [1,2,3,4,5,6,7,8,9].
        wearposition (Union[Unset, int]): Where the user is wearing the device.


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
             Example: 1.
    """

    sampling_frequency: Union[Unset, int] = UNSET
    signal: Union[Unset, list[int]] = UNSET
    wearposition: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sampling_frequency = self.sampling_frequency

        signal: Union[Unset, list[int]] = UNSET
        if not isinstance(self.signal, Unset):
            signal = self.signal

        wearposition = self.wearposition

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sampling_frequency is not UNSET:
            field_dict["sampling_frequency"] = sampling_frequency
        if signal is not UNSET:
            field_dict["signal"] = signal
        if wearposition is not UNSET:
            field_dict["wearposition"] = wearposition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        sampling_frequency = d.pop("sampling_frequency", UNSET)

        signal = cast(list[int], d.pop("signal", UNSET))

        wearposition = d.pop("wearposition", UNSET)

        heartv_2_get_response_200_body = cls(
            sampling_frequency=sampling_frequency,
            signal=signal,
            wearposition=wearposition,
        )

        heartv_2_get_response_200_body.additional_properties = d
        return heartv_2_get_response_200_body

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
