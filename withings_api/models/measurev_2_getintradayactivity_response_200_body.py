from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measurev_2_getintradayactivity_response_200_body_series import (
        Measurev2GetintradayactivityResponse200BodySeries,
    )


T = TypeVar("T", bound="Measurev2GetintradayactivityResponse200Body")


@_attrs_define
class Measurev2GetintradayactivityResponse200Body:
    """Response data.

    Attributes:
        series (Union[Unset, Measurev2GetintradayactivityResponse200BodySeries]):
    """

    series: Union[Unset, "Measurev2GetintradayactivityResponse200BodySeries"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.measurev_2_getintradayactivity_response_200_body_series import (
            Measurev2GetintradayactivityResponse200BodySeries,
        )

        d = src_dict.copy()
        _series = d.pop("series", UNSET)
        series: Union[Unset, Measurev2GetintradayactivityResponse200BodySeries]
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = Measurev2GetintradayactivityResponse200BodySeries.from_dict(_series)

        measurev_2_getintradayactivity_response_200_body = cls(
            series=series,
        )

        measurev_2_getintradayactivity_response_200_body.additional_properties = d
        return measurev_2_getintradayactivity_response_200_body

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
