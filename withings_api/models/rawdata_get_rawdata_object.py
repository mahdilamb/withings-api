from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RawdataGetRawdataObject")


@_attrs_define
class RawdataGetRawdataObject:
    """
    Attributes:
        data (Union[Unset, str]):
        enddate (Union[Unset, int]): The end datetime for the sleep data. A single call can span up to 7 days maximum.
            To cover a wider time range, you will need to perform multiple calls.
        firmware_version (Union[Unset, int]):
        format_version (Union[Unset, int]):
        hash_deviceid (Union[Unset, str]): ID of the device. This ID is returned in other services to know which device
            tracked a data. Then device's model or type can be known using this information.
        sensor_name (Union[Unset, str]):
        startdate (Union[Unset, int]): The starting datetime for the sleep state data.
        type_ (Union[Unset, int]): Type of the measure. See ```meastype``` input parameter.
    """

    data: Union[Unset, str] = UNSET
    enddate: Union[Unset, int] = UNSET
    firmware_version: Union[Unset, int] = UNSET
    format_version: Union[Unset, int] = UNSET
    hash_deviceid: Union[Unset, str] = UNSET
    sensor_name: Union[Unset, str] = UNSET
    startdate: Union[Unset, int] = UNSET
    type_: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        enddate = self.enddate

        firmware_version = self.firmware_version

        format_version = self.format_version

        hash_deviceid = self.hash_deviceid

        sensor_name = self.sensor_name

        startdate = self.startdate

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if enddate is not UNSET:
            field_dict["enddate"] = enddate
        if firmware_version is not UNSET:
            field_dict["firmware_version"] = firmware_version
        if format_version is not UNSET:
            field_dict["format_version"] = format_version
        if hash_deviceid is not UNSET:
            field_dict["hash_deviceid"] = hash_deviceid
        if sensor_name is not UNSET:
            field_dict["sensor_name"] = sensor_name
        if startdate is not UNSET:
            field_dict["startdate"] = startdate
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        data = d.pop("data", UNSET)

        enddate = d.pop("enddate", UNSET)

        firmware_version = d.pop("firmware_version", UNSET)

        format_version = d.pop("format_version", UNSET)

        hash_deviceid = d.pop("hash_deviceid", UNSET)

        sensor_name = d.pop("sensor_name", UNSET)

        startdate = d.pop("startdate", UNSET)

        type_ = d.pop("type", UNSET)

        rawdata_get_rawdata_object = cls(
            data=data,
            enddate=enddate,
            firmware_version=firmware_version,
            format_version=format_version,
            hash_deviceid=hash_deviceid,
            sensor_name=sensor_name,
            startdate=startdate,
            type_=type_,
        )

        rawdata_get_rawdata_object.additional_properties = d
        return rawdata_get_rawdata_object

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
