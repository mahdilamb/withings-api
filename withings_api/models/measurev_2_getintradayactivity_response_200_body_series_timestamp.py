from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Measurev2GetintradayactivityResponse200BodySeriesTimestamp")


@_attrs_define
class Measurev2GetintradayactivityResponse200BodySeriesTimestamp:
    """$timestamp represents the epoch value of the intraday data

    Attributes:
        calories (Union[Unset, float]): Estimation of active calories burned (in Kcal). *(Use 'data_fields' to request
            this data.)*
        deviceid (Union[Unset, str]): ID of device that tracked the data. To retrieve information about this device,
            refer to : <a href='/api-reference/#operation/userv2-getdevice'>User v2 - Getdevice</a>. Example:
            892359876fd8805ac45bab078c4828692f0276b1.
        distance (Union[Unset, float]): Distance travelled (in meters). *(Use 'data_fields' to request this data.)*
        duration (Union[Unset, int]): Duration of the activity (in seconds). *(Use 'data_fields' to request this data.)*
        elevation (Union[Unset, float]): Number of floors climbed. *(Use 'data_fields' to request this data.)*
        heart_rate (Union[Unset, int]): Measured heart rate. *(Use 'data_fields' to request this data.)*
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
             Example: Pulse.
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
             Example: 51.
        pool_lap (Union[Unset, int]): Number of pool_lap performed. *(Use 'data_fields' to request this data.)*
        spo2_auto (Union[Unset, float]): SpO2 measurement automatically tracked by a device tracker
        steps (Union[Unset, int]): Number of steps. *(Use 'data_fields' to request this data.)*
        stroke (Union[Unset, int]): Number of strokes performed. *(Use 'data_fields' to request this data.)*
    """

    calories: Union[Unset, float] = UNSET
    deviceid: Union[Unset, str] = UNSET
    distance: Union[Unset, float] = UNSET
    duration: Union[Unset, int] = UNSET
    elevation: Union[Unset, float] = UNSET
    heart_rate: Union[Unset, int] = UNSET
    model: Union[Unset, str] = UNSET
    model_id: Union[Unset, int] = UNSET
    pool_lap: Union[Unset, int] = UNSET
    spo2_auto: Union[Unset, float] = UNSET
    steps: Union[Unset, int] = UNSET
    stroke: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calories = self.calories

        deviceid = self.deviceid

        distance = self.distance

        duration = self.duration

        elevation = self.elevation

        heart_rate = self.heart_rate

        model = self.model

        model_id = self.model_id

        pool_lap = self.pool_lap

        spo2_auto = self.spo2_auto

        steps = self.steps

        stroke = self.stroke

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if calories is not UNSET:
            field_dict["calories"] = calories
        if deviceid is not UNSET:
            field_dict["deviceid"] = deviceid
        if distance is not UNSET:
            field_dict["distance"] = distance
        if duration is not UNSET:
            field_dict["duration"] = duration
        if elevation is not UNSET:
            field_dict["elevation"] = elevation
        if heart_rate is not UNSET:
            field_dict["heart_rate"] = heart_rate
        if model is not UNSET:
            field_dict["model"] = model
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if pool_lap is not UNSET:
            field_dict["pool_lap"] = pool_lap
        if spo2_auto is not UNSET:
            field_dict["spo2_auto"] = spo2_auto
        if steps is not UNSET:
            field_dict["steps"] = steps
        if stroke is not UNSET:
            field_dict["stroke"] = stroke

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        calories = d.pop("calories", UNSET)

        deviceid = d.pop("deviceid", UNSET)

        distance = d.pop("distance", UNSET)

        duration = d.pop("duration", UNSET)

        elevation = d.pop("elevation", UNSET)

        heart_rate = d.pop("heart_rate", UNSET)

        model = d.pop("model", UNSET)

        model_id = d.pop("model_id", UNSET)

        pool_lap = d.pop("pool_lap", UNSET)

        spo2_auto = d.pop("spo2_auto", UNSET)

        steps = d.pop("steps", UNSET)

        stroke = d.pop("stroke", UNSET)

        measurev_2_getintradayactivity_response_200_body_series_timestamp = cls(
            calories=calories,
            deviceid=deviceid,
            distance=distance,
            duration=duration,
            elevation=elevation,
            heart_rate=heart_rate,
            model=model,
            model_id=model_id,
            pool_lap=pool_lap,
            spo2_auto=spo2_auto,
            steps=steps,
            stroke=stroke,
        )

        measurev_2_getintradayactivity_response_200_body_series_timestamp.additional_properties = d
        return measurev_2_getintradayactivity_response_200_body_series_timestamp

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
