from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Stethov2GetResponse200Body")


@_attrs_define
class Stethov2GetResponse200Body:
    """Response data.

    Attributes:
        channel (Union[Unset, int]):  Example: 1.
        duration (Union[Unset, int]): Duration of the signal Example: 1.
        format_ (Union[Unset, int]):  Example: 1.
        frequency (Union[Unset, int]): Frequency of the stetho signal, usually 4kHz Example: 1.
        model (Union[Unset, int]): Device model returning this signal (71 for Beamo, 44 for BPM  Core) Example: 1.
        resolution (Union[Unset, int]):  Example: 1.
        signal (Union[Unset, list[int]]): A-law G 711 encoded signal (See [here](/developer-guide/v3/get-signal/decode-
            stetho-to-pcm) to understand how to decode it in PCM) Example: [1,2,3,4,5,6,7,8,9].
        size (Union[Unset, int]):  Example: 1.
        vhd (Union[Unset, int]):  Example: 1.
    """

    channel: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    format_: Union[Unset, int] = UNSET
    frequency: Union[Unset, int] = UNSET
    model: Union[Unset, int] = UNSET
    resolution: Union[Unset, int] = UNSET
    signal: Union[Unset, list[int]] = UNSET
    size: Union[Unset, int] = UNSET
    vhd: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        duration = self.duration

        format_ = self.format_

        frequency = self.frequency

        model = self.model

        resolution = self.resolution

        signal: Union[Unset, list[int]] = UNSET
        if not isinstance(self.signal, Unset):
            signal = self.signal

        size = self.size

        vhd = self.vhd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if duration is not UNSET:
            field_dict["duration"] = duration
        if format_ is not UNSET:
            field_dict["format"] = format_
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if model is not UNSET:
            field_dict["model"] = model
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if signal is not UNSET:
            field_dict["signal"] = signal
        if size is not UNSET:
            field_dict["size"] = size
        if vhd is not UNSET:
            field_dict["vhd"] = vhd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        channel = d.pop("channel", UNSET)

        duration = d.pop("duration", UNSET)

        format_ = d.pop("format", UNSET)

        frequency = d.pop("frequency", UNSET)

        model = d.pop("model", UNSET)

        resolution = d.pop("resolution", UNSET)

        signal = cast(list[int], d.pop("signal", UNSET))

        size = d.pop("size", UNSET)

        vhd = d.pop("vhd", UNSET)

        stethov_2_get_response_200_body = cls(
            channel=channel,
            duration=duration,
            format_=format_,
            frequency=frequency,
            model=model,
            resolution=resolution,
            signal=signal,
            size=size,
            vhd=vhd,
        )

        stethov_2_get_response_200_body.additional_properties = d
        return stethov_2_get_response_200_body

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
