from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.heart_measurement_object_bloodpressure import HeartMeasurementObjectBloodpressure
    from ..models.heart_measurement_object_ecg import HeartMeasurementObjectEcg


T = TypeVar("T", bound="HeartMeasurementObject")


@_attrs_define
class HeartMeasurementObject:
    """
    Attributes:
        bloodpressure (Union[Unset, HeartMeasurementObjectBloodpressure]):
        deviceid (Union[Unset, str]): ID of device that tracked the data. To retrieve information about this device,
            refer to : <a href='/api-reference/#operation/userv2-getdevice'>User v2 - Getdevice</a>.
        ecg (Union[Unset, HeartMeasurementObjectEcg]):
        heart_rate (Union[Unset, int]): Average recorded heart rate.
        model (Union[Unset, int]): The source of the recording.


            | Value | Description|
            |---|---|
            |44 | BPM Core|
            |91 | Move ECG|
        timestamp (Union[Unset, int]): Timestamp of the recording.
        timezone (Union[Unset, str]): Timezone for the date.
    """

    bloodpressure: Union[Unset, "HeartMeasurementObjectBloodpressure"] = UNSET
    deviceid: Union[Unset, str] = UNSET
    ecg: Union[Unset, "HeartMeasurementObjectEcg"] = UNSET
    heart_rate: Union[Unset, int] = UNSET
    model: Union[Unset, int] = UNSET
    timestamp: Union[Unset, int] = UNSET
    timezone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bloodpressure: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bloodpressure, Unset):
            bloodpressure = self.bloodpressure.to_dict()

        deviceid = self.deviceid

        ecg: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ecg, Unset):
            ecg = self.ecg.to_dict()

        heart_rate = self.heart_rate

        model = self.model

        timestamp = self.timestamp

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bloodpressure is not UNSET:
            field_dict["bloodpressure"] = bloodpressure
        if deviceid is not UNSET:
            field_dict["deviceid"] = deviceid
        if ecg is not UNSET:
            field_dict["ecg"] = ecg
        if heart_rate is not UNSET:
            field_dict["heart_rate"] = heart_rate
        if model is not UNSET:
            field_dict["model"] = model
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.heart_measurement_object_bloodpressure import HeartMeasurementObjectBloodpressure
        from ..models.heart_measurement_object_ecg import HeartMeasurementObjectEcg

        d = src_dict.copy()
        _bloodpressure = d.pop("bloodpressure", UNSET)
        bloodpressure: Union[Unset, HeartMeasurementObjectBloodpressure]
        if isinstance(_bloodpressure, Unset):
            bloodpressure = UNSET
        else:
            bloodpressure = HeartMeasurementObjectBloodpressure.from_dict(_bloodpressure)

        deviceid = d.pop("deviceid", UNSET)

        _ecg = d.pop("ecg", UNSET)
        ecg: Union[Unset, HeartMeasurementObjectEcg]
        if isinstance(_ecg, Unset):
            ecg = UNSET
        else:
            ecg = HeartMeasurementObjectEcg.from_dict(_ecg)

        heart_rate = d.pop("heart_rate", UNSET)

        model = d.pop("model", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        timezone = d.pop("timezone", UNSET)

        heart_measurement_object = cls(
            bloodpressure=bloodpressure,
            deviceid=deviceid,
            ecg=ecg,
            heart_rate=heart_rate,
            model=model,
            timestamp=timestamp,
            timezone=timezone,
        )

        heart_measurement_object.additional_properties = d
        return heart_measurement_object

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
