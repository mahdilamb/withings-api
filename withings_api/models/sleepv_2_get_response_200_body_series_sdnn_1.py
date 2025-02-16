from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Sleepv2GetResponse200BodySeriesSdnn1")


@_attrs_define
class Sleepv2GetResponse200BodySeriesSdnn1:
    """Heart rate variability - Standard deviation of the NN over 1 minute

    Attributes:
        timestamp (Union[Unset, int]):
    """

    timestamp: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["$timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = d.pop("$timestamp", UNSET)

        sleepv_2_get_response_200_body_series_sdnn_1 = cls(
            timestamp=timestamp,
        )

        sleepv_2_get_response_200_body_series_sdnn_1.additional_properties = d
        return sleepv_2_get_response_200_body_series_sdnn_1

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
