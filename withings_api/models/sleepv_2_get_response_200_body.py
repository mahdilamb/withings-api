from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sleepv_2_get_response_200_body_series import Sleepv2GetResponse200BodySeries


T = TypeVar("T", bound="Sleepv2GetResponse200Body")


@_attrs_define
class Sleepv2GetResponse200Body:
    """Response data.

    Attributes:
        series (Union[Unset, Sleepv2GetResponse200BodySeries]):
    """

    series: Union[Unset, "Sleepv2GetResponse200BodySeries"] = UNSET
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
        from ..models.sleepv_2_get_response_200_body_series import Sleepv2GetResponse200BodySeries

        d = src_dict.copy()
        _series = d.pop("series", UNSET)
        series: Union[Unset, Sleepv2GetResponse200BodySeries]
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = Sleepv2GetResponse200BodySeries.from_dict(_series)

        sleepv_2_get_response_200_body = cls(
            series=series,
        )

        sleepv_2_get_response_200_body.additional_properties = d
        return sleepv_2_get_response_200_body

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
