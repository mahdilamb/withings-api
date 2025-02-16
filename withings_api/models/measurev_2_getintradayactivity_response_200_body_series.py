from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measurev_2_getintradayactivity_response_200_body_series_timestamp import (
        Measurev2GetintradayactivityResponse200BodySeriesTimestamp,
    )


T = TypeVar("T", bound="Measurev2GetintradayactivityResponse200BodySeries")


@_attrs_define
class Measurev2GetintradayactivityResponse200BodySeries:
    """
    Attributes:
        timestamp (Union[Unset, Measurev2GetintradayactivityResponse200BodySeriesTimestamp]): $timestamp represents the
            epoch value of the intraday data
    """

    timestamp: Union[Unset, "Measurev2GetintradayactivityResponse200BodySeriesTimestamp"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["$timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.measurev_2_getintradayactivity_response_200_body_series_timestamp import (
            Measurev2GetintradayactivityResponse200BodySeriesTimestamp,
        )

        d = src_dict.copy()
        _timestamp = d.pop("$timestamp", UNSET)
        timestamp: Union[Unset, Measurev2GetintradayactivityResponse200BodySeriesTimestamp]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = Measurev2GetintradayactivityResponse200BodySeriesTimestamp.from_dict(_timestamp)

        measurev_2_getintradayactivity_response_200_body_series = cls(
            timestamp=timestamp,
        )

        measurev_2_getintradayactivity_response_200_body_series.additional_properties = d
        return measurev_2_getintradayactivity_response_200_body_series

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
