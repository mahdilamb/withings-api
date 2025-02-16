from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StethoMeasurementObject")


@_attrs_define
class StethoMeasurementObject:
    """
    Attributes:
        hash_deviceid (Union[Unset, str]): ID of device that tracked the data. To retrieve information about this
            device, refer to : <a href='/api-reference/#operation/userv2-getdevice'>User v2 - Getdevice</a>.
        signalid (Union[Unset, int]): Id of the signal.
        timestamp (Union[Unset, int]): Timestamp of the recording.
        timezone (Union[Unset, str]): Timezone for the date.
        vhd (Union[Unset, int]):
    """

    hash_deviceid: Union[Unset, str] = UNSET
    signalid: Union[Unset, int] = UNSET
    timestamp: Union[Unset, int] = UNSET
    timezone: Union[Unset, str] = UNSET
    vhd: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_deviceid = self.hash_deviceid

        signalid = self.signalid

        timestamp = self.timestamp

        timezone = self.timezone

        vhd = self.vhd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hash_deviceid is not UNSET:
            field_dict["hash_deviceid"] = hash_deviceid
        if signalid is not UNSET:
            field_dict["signalid"] = signalid
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if vhd is not UNSET:
            field_dict["vhd"] = vhd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        hash_deviceid = d.pop("hash_deviceid", UNSET)

        signalid = d.pop("signalid", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        timezone = d.pop("timezone", UNSET)

        vhd = d.pop("vhd", UNSET)

        stetho_measurement_object = cls(
            hash_deviceid=hash_deviceid,
            signalid=signalid,
            timestamp=timestamp,
            timezone=timezone,
            vhd=vhd,
        )

        stetho_measurement_object.additional_properties = d
        return stetho_measurement_object

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
