from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measure_object import MeasureObject


T = TypeVar("T", bound="MeasuregrpObject")


@_attrs_define
class MeasuregrpObject:
    """
    Attributes:
        attrib (Union[Unset, int]): The way the measure was attributed to the user:


            | Value | Description|
            |---|---|
            |0 | The measuregroup has been captured by a device and is known to belong to this user (and is not ambiguous)|
            |1 | The measuregroup has been captured by a device but may belong to other users as well as this one (it is
            ambiguous)|
            |2 | The measuregroup has been entered manually for this particular user|
            |4 | The measuregroup has been entered manually during user creation (and may not be accurate)|
            |5 | Measure auto, it's only for the Blood Pressure Monitor. This device can make many measures and computed the
            best value|
            |7 | Measure confirmed. You can get this value if the user confirmed a detected activity|
            |8 | Same as attrib 0|
            |15 | The measure has been performed in specific guided conditions. Apply to Nerve Health Score|
            |17 | The measure has been performed in specific guided conditions. Apply to Nerve Health Score and
            Electrochemical Skin Conductance|
        category (Union[Unset, int]): Category for the measures in the group (see category input parameter).
        comment (Union[Unset, str]): Deprecated. This property will always be empty.
        created (Union[Unset, int]): UNIX timestamp when measures were stored.
        date (Union[Unset, int]): UNIX timestamp when measures were taken.
        deviceid (Union[Unset, str]): ID of device that tracked the data. To retrieve information about this device,
            refer to : <a href='/api-reference/#operation/userv2-getdevice'>User v2 - Getdevice</a>.
        grpid (Union[Unset, int]): Unique identifier of the measure group.
        hash_deviceid (Union[Unset, str]): ID of device that tracked the data. To retrieve information about this
            device, refer to : <a href='/api-reference/#operation/userv2-getdevice'>User v2 - Getdevice</a>.
        measures (Union[Unset, list['MeasureObject']]): List of measures in the group.
        modified (Union[Unset, int]): UNIX timestamp when measures were last updated.
        timezone (Union[Unset, str]): Timezone for the date.
    """

    attrib: Union[Unset, int] = UNSET
    category: Union[Unset, int] = UNSET
    comment: Union[Unset, str] = UNSET
    created: Union[Unset, int] = UNSET
    date: Union[Unset, int] = UNSET
    deviceid: Union[Unset, str] = UNSET
    grpid: Union[Unset, int] = UNSET
    hash_deviceid: Union[Unset, str] = UNSET
    measures: Union[Unset, list["MeasureObject"]] = UNSET
    modified: Union[Unset, int] = UNSET
    timezone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attrib = self.attrib

        category = self.category

        comment = self.comment

        created = self.created

        date = self.date

        deviceid = self.deviceid

        grpid = self.grpid

        hash_deviceid = self.hash_deviceid

        measures: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.measures, Unset):
            measures = []
            for measures_item_data in self.measures:
                measures_item = measures_item_data.to_dict()
                measures.append(measures_item)

        modified = self.modified

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attrib is not UNSET:
            field_dict["attrib"] = attrib
        if category is not UNSET:
            field_dict["category"] = category
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created is not UNSET:
            field_dict["created"] = created
        if date is not UNSET:
            field_dict["date"] = date
        if deviceid is not UNSET:
            field_dict["deviceid"] = deviceid
        if grpid is not UNSET:
            field_dict["grpid"] = grpid
        if hash_deviceid is not UNSET:
            field_dict["hash_deviceid"] = hash_deviceid
        if measures is not UNSET:
            field_dict["measures"] = measures
        if modified is not UNSET:
            field_dict["modified"] = modified
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.measure_object import MeasureObject

        d = src_dict.copy()
        attrib = d.pop("attrib", UNSET)

        category = d.pop("category", UNSET)

        comment = d.pop("comment", UNSET)

        created = d.pop("created", UNSET)

        date = d.pop("date", UNSET)

        deviceid = d.pop("deviceid", UNSET)

        grpid = d.pop("grpid", UNSET)

        hash_deviceid = d.pop("hash_deviceid", UNSET)

        measures = []
        _measures = d.pop("measures", UNSET)
        for measures_item_data in _measures or []:
            measures_item = MeasureObject.from_dict(measures_item_data)

            measures.append(measures_item)

        modified = d.pop("modified", UNSET)

        timezone = d.pop("timezone", UNSET)

        measuregrp_object = cls(
            attrib=attrib,
            category=category,
            comment=comment,
            created=created,
            date=date,
            deviceid=deviceid,
            grpid=grpid,
            hash_deviceid=hash_deviceid,
            measures=measures,
            modified=modified,
            timezone=timezone,
        )

        measuregrp_object.additional_properties = d
        return measuregrp_object

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
