from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DropshipmentGetOrderStatusProductDeviceObject")


@_attrs_define
class DropshipmentGetOrderStatusProductDeviceObject:
    """
    Attributes:
        hash_deviceid (Union[Unset, str]): ID of the device. This ID is returned in other services to know which device
            tracked a data. Then device's model or type can be known using this information.
        mac_address (Union[Unset, str]): Mac address of the device.
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
        serial_number (Union[Unset, str]): Serial number of the device.
    """

    hash_deviceid: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    model_id: Union[Unset, int] = UNSET
    serial_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_deviceid = self.hash_deviceid

        mac_address = self.mac_address

        model = self.model

        model_id = self.model_id

        serial_number = self.serial_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hash_deviceid is not UNSET:
            field_dict["hash_deviceid"] = hash_deviceid
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if model is not UNSET:
            field_dict["model"] = model
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        hash_deviceid = d.pop("hash_deviceid", UNSET)

        mac_address = d.pop("mac_address", UNSET)

        model = d.pop("model", UNSET)

        model_id = d.pop("model_id", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        dropshipment_get_order_status_product_device_object = cls(
            hash_deviceid=hash_deviceid,
            mac_address=mac_address,
            model=model,
            model_id=model_id,
            serial_number=serial_number,
        )

        dropshipment_get_order_status_product_device_object.additional_properties = d
        return dropshipment_get_order_status_product_device_object

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
