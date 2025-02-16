from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measuregrp_object import MeasuregrpObject


T = TypeVar("T", bound="MeasureGetmeasResponse200Body")


@_attrs_define
class MeasureGetmeasResponse200Body:
    """Response data.

    Attributes:
        measuregrps (Union[Unset, list['MeasuregrpObject']]): For every measure/measurement made, a measure group is
            created. The measure group purpose is to group together measures that have been taken at the same time. For
            instance, when measuring blood pressure you will have a measure group with a systole measure, a diastole
            measure, and a heartrate measure. Every time a measure is create/updated/deleted, the corresponding measure
            group is updated.
        more (Union[Unset, int]): To know if there is more data to fetch or not.
        offset (Union[Unset, int]): Offset to use to retrieve the next data.
        timezone (Union[Unset, str]): Timezone for the date.
        updatetime (Union[Unset, str]): Server time at which the answer was generated.
    """

    measuregrps: Union[Unset, list["MeasuregrpObject"]] = UNSET
    more: Union[Unset, int] = UNSET
    offset: Union[Unset, int] = UNSET
    timezone: Union[Unset, str] = UNSET
    updatetime: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measuregrps: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.measuregrps, Unset):
            measuregrps = []
            for measuregrps_item_data in self.measuregrps:
                measuregrps_item = measuregrps_item_data.to_dict()
                measuregrps.append(measuregrps_item)

        more = self.more

        offset = self.offset

        timezone = self.timezone

        updatetime = self.updatetime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measuregrps is not UNSET:
            field_dict["measuregrps"] = measuregrps
        if more is not UNSET:
            field_dict["more"] = more
        if offset is not UNSET:
            field_dict["offset"] = offset
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if updatetime is not UNSET:
            field_dict["updatetime"] = updatetime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.measuregrp_object import MeasuregrpObject

        d = src_dict.copy()
        measuregrps = []
        _measuregrps = d.pop("measuregrps", UNSET)
        for measuregrps_item_data in _measuregrps or []:
            measuregrps_item = MeasuregrpObject.from_dict(measuregrps_item_data)

            measuregrps.append(measuregrps_item)

        more = d.pop("more", UNSET)

        offset = d.pop("offset", UNSET)

        timezone = d.pop("timezone", UNSET)

        updatetime = d.pop("updatetime", UNSET)

        measure_getmeas_response_200_body = cls(
            measuregrps=measuregrps,
            more=more,
            offset=offset,
            timezone=timezone,
            updatetime=updatetime,
        )

        measure_getmeas_response_200_body.additional_properties = d
        return measure_getmeas_response_200_body

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
