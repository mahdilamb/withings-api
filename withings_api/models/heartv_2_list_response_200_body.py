from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.heart_measurement_object import HeartMeasurementObject


T = TypeVar("T", bound="Heartv2ListResponse200Body")


@_attrs_define
class Heartv2ListResponse200Body:
    """Response data.

    Attributes:
        more (Union[Unset, bool]): To know if there is more data to fetch or not.
        offset (Union[Unset, int]): Offset to use to retrieve the next data.
        series (Union[Unset, list['HeartMeasurementObject']]):
    """

    more: Union[Unset, bool] = UNSET
    offset: Union[Unset, int] = UNSET
    series: Union[Unset, list["HeartMeasurementObject"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        more = self.more

        offset = self.offset

        series: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if more is not UNSET:
            field_dict["more"] = more
        if offset is not UNSET:
            field_dict["offset"] = offset
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.heart_measurement_object import HeartMeasurementObject

        d = src_dict.copy()
        more = d.pop("more", UNSET)

        offset = d.pop("offset", UNSET)

        series = []
        _series = d.pop("series", UNSET)
        for series_item_data in _series or []:
            series_item = HeartMeasurementObject.from_dict(series_item_data)

            series.append(series_item)

        heartv_2_list_response_200_body = cls(
            more=more,
            offset=offset,
            series=series,
        )

        heartv_2_list_response_200_body.additional_properties = d
        return heartv_2_list_response_200_body

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
