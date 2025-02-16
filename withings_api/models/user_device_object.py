from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDeviceObject")


@_attrs_define
class UserDeviceObject:
    """
    Attributes:
        battery (Union[Unset, str]): Battery level: high (> 75%), medium (> 30%) or low
        deviceid (Union[Unset, str]): ID of the device. This ID is returned in other services to know which device
            tracked a data. Then device's model or type can be known using this information.
        first_session_date (Union[Unset, int]): The timestamp of the first server connection of the device
        fw (Union[Unset, str]): Device's firmware (advanced partners only).
        hash_deviceid (Union[Unset, str]): ID of the device. This ID is returned in other services to know which device
            tracked a data. Then device's model or type can be known using this information.
        last_session_date (Union[Unset, int]): The timestamp of the last server connection of the device
        last_used_network (Union[Unset, str]): Last network used by the device (advanced partners only).
        mac_address (Union[Unset, str]): Mac address of the device (advanced partners only).
        model (Union[Unset, str]): Device model. Value can be:


            | Value | Description|
            |---|---|
            |Withings WBS01 | Scale|
            |WS30 | Scale|
            |Kid Scale | Scale|
            |Smart Body Analyzer | Scale|
            |Body+ | Scale|
            |Body Cardio | Scale|
            |Body | Scale|
            |Body Scan | Scale|
            |Body Pro | Scale|
            |WBS10 | Scale|
            |WBS11 | Scale|
            |Smart Baby Monitor | Babyphone|
            |Withings Home | Babyphone|
            |Withings Blood Pressure Monitor V1 | Blood Pressure Monitor|
            |Withings Blood Pressure Monitor V2 | Blood Pressure Monitor|
            |Withings Blood Pressure Monitor V3 | Blood Pressure Monitor|
            |BPM Core | Blood Pressure Monitor|
            |BPM Connect | Blood Pressure Monitor|
            |BPM Connect Pro | Blood Pressure Monitor|
            |BPM Pro 2 | Blood Pressure Monitor|
            |BPM Vision | Blood Pressure Monitor|
            |Pulse | Activity Tracker|
            |Activite | Activity Tracker|
            |Activite (Pop, Steel) | Activity Tracker|
            |Withings Go | Activity Tracker|
            |Activite Steel HR | Activity Tracker|
            |Activite Steel HR Sport Edition | Activity Tracker|
            |Pulse HR | Activity Tracker|
            |Move | Activity Tracker|
            |Move ECG | Activity Tracker|
            |ScanWatch | Activity Tracker|
            |ScanWatch 2 | Activity Tracker|
            |ScanWatch Light | Activity Tracker|
            |Aura Dock | Sleep Monitor|
            |Aura Sensor | Sleep Monitor|
            |Aura Sensor V2 | Sleep Monitor|
            |Thermo | Smart Connected Thermometer|
            |WUP01 | Gateway|
            |Iglucose glucometer | iGlucose|
            |iOS step tracker | HealthKit Apple|
            |HealthKit step iPhone tracker | HealthKit Apple|
            |HealthKit step Apple Watch tracker | HealthKit Apple|
            |HealthKit other step tracker | HealthKit Apple|
            |Android step tracker | HealthKit Google|
            |GoogleFit tracker | HealthKit Google|
            |Samsung Health tracker | HealthKit Google|
            |Huawei tracker | HealthKit Huawei|
        model_id (Union[Unset, int]):

            | Value | Description|
            |---|---|
            |1 | Withings WBS01|
            |2 | WS30|
            |3 | Kid Scale|
            |4 | Smart Body Analyzer|
            |5 | Body+|
            |6 | Body Cardio|
            |7 | Body|
            |10 | Body Scan|
            |9 | Body Pro|
            |11 | WBS10|
            |12 | WBS11|
            |21 | Smart Baby Monitor|
            |22 | Withings Home|
            |41 | Withings Blood Pressure Monitor V1|
            |42 | Withings Blood Pressure Monitor V2|
            |43 | Withings Blood Pressure Monitor V3|
            |44 | BPM Core|
            |45 | BPM Connect|
            |46 | BPM Connect Pro|
            |47 | BPM Pro 2|
            |48 | BPM Vision|
            |51 | Pulse|
            |52 | Activite|
            |53 | Activite (Pop, Steel)|
            |54 | Withings Go|
            |55 | Activite Steel HR|
            |59 | Activite Steel HR Sport Edition|
            |58 | Pulse HR|
            |90 | Move|
            |91 | Move ECG|
            |92 | Move ECG|
            |93 | ScanWatch|
            |94 | ScanWatch 2|
            |95 | ScanWatch Light|
            |60 | Aura Dock|
            |61 | Aura Sensor|
            |63 | Aura Sensor V2|
            |70 | Thermo|
            |100 | WUP01|
            |1061 | Iglucose glucometer|
            |1051 | iOS step tracker|
            |1052 | iOS step tracker|
            |1057 | HealthKit step iPhone tracker|
            |1058 | HealthKit step Apple Watch tracker|
            |1059 | HealthKit other step tracker|
            |1053 | Android step tracker|
            |1054 | Android step tracker|
            |1055 | GoogleFit tracker|
            |1056 | Samsung Health tracker|
            |1060 | Android step tracker|
            |1062 | Huawei tracker|
        network (Union[Unset, str]): Network used by the device (advanced partners only).
        timezone (Union[Unset, str]): Timezone of the device.
        type_ (Union[Unset, str]): Type of the device. Value can be:


            | Value|
            |---|
            |Scale|
            |Babyphone|
            |Blood Pressure Monitor|
            |Activity Tracker|
            |Sleep Monitor|
            |Smart Connected Thermometer|
            |Gateway|
            |iGlucose|
            |HealthKit Apple|
            |HealthKit Google|
            |HealthKit Huawei|
    """

    battery: Union[Unset, str] = UNSET
    deviceid: Union[Unset, str] = UNSET
    first_session_date: Union[Unset, int] = UNSET
    fw: Union[Unset, str] = UNSET
    hash_deviceid: Union[Unset, str] = UNSET
    last_session_date: Union[Unset, int] = UNSET
    last_used_network: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    model_id: Union[Unset, int] = UNSET
    network: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        battery = self.battery

        deviceid = self.deviceid

        first_session_date = self.first_session_date

        fw = self.fw

        hash_deviceid = self.hash_deviceid

        last_session_date = self.last_session_date

        last_used_network = self.last_used_network

        mac_address = self.mac_address

        model = self.model

        model_id = self.model_id

        network = self.network

        timezone = self.timezone

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if battery is not UNSET:
            field_dict["battery"] = battery
        if deviceid is not UNSET:
            field_dict["deviceid"] = deviceid
        if first_session_date is not UNSET:
            field_dict["first_session_date"] = first_session_date
        if fw is not UNSET:
            field_dict["fw"] = fw
        if hash_deviceid is not UNSET:
            field_dict["hash_deviceid"] = hash_deviceid
        if last_session_date is not UNSET:
            field_dict["last_session_date"] = last_session_date
        if last_used_network is not UNSET:
            field_dict["last_used_network"] = last_used_network
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if model is not UNSET:
            field_dict["model"] = model
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if network is not UNSET:
            field_dict["network"] = network
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        battery = d.pop("battery", UNSET)

        deviceid = d.pop("deviceid", UNSET)

        first_session_date = d.pop("first_session_date", UNSET)

        fw = d.pop("fw", UNSET)

        hash_deviceid = d.pop("hash_deviceid", UNSET)

        last_session_date = d.pop("last_session_date", UNSET)

        last_used_network = d.pop("last_used_network", UNSET)

        mac_address = d.pop("mac_address", UNSET)

        model = d.pop("model", UNSET)

        model_id = d.pop("model_id", UNSET)

        network = d.pop("network", UNSET)

        timezone = d.pop("timezone", UNSET)

        type_ = d.pop("type", UNSET)

        user_device_object = cls(
            battery=battery,
            deviceid=deviceid,
            first_session_date=first_session_date,
            fw=fw,
            hash_deviceid=hash_deviceid,
            last_session_date=last_session_date,
            last_used_network=last_used_network,
            mac_address=mac_address,
            model=model,
            model_id=model_id,
            network=network,
            timezone=timezone,
            type_=type_,
        )

        user_device_object.additional_properties = d
        return user_device_object

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
