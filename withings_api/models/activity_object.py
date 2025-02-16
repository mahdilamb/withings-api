from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityObject")


@_attrs_define
class ActivityObject:
    """
    Attributes:
        active (Union[Unset, int]): Sum of intense and moderate activity durations (in seconds). *(Use 'data_fields' to
            request this data.)*
        brand (Union[Unset, int]): Specifies if data comes from Withings (device or mobile application tracker) or an
            external way (Value is 1 for Withings and 18 for external)
        calories (Union[Unset, float]): Active calories burned (in Kcal). Calculated by mixing fine granularity calories
            estimation, workouts estimated calories and calories manually set by the user. *(Use 'data_fields' to request
            this data.)*
        date (Union[Unset, str]): Date of the aggregated data.
        deviceid (Union[Unset, str]): ID of device that tracked the data. To retrieve information about this device,
            refer to : <a href='/api-reference/#operation/userv2-getdevice'>User v2 - Getdevice</a>.
        distance (Union[Unset, float]): Distance travelled (in meters). *(Use 'data_fields' to request this data.)*
        elevation (Union[Unset, float]): Number of floors climbed. *(Use 'data_fields' to request this data.)*
        hash_deviceid (Union[Unset, str]): ID of device that tracked the data. To retrieve information about this
            device, refer to : <a href='/api-reference/#operation/userv2-getdevice'>User v2 - Getdevice</a>.
        hr_average (Union[Unset, int]): Average heart rate. *(Use 'data_fields' to request this data.)*
        hr_max (Union[Unset, int]): Maximal heart rate. *(Use 'data_fields' to request this data.)*
        hr_min (Union[Unset, int]): Minimal heart rate. *(Use 'data_fields' to request this data.)*
        hr_zone_0 (Union[Unset, int]): Duration in seconds when heart rate was in a light zone (cf. <a href='/api-
            reference/#section/Glossary'>Glossary</a>). *(Use 'data_fields' to request this data.)*
        hr_zone_1 (Union[Unset, int]): Duration in seconds when heart rate was in a moderate zone (cf. <a href='/api-
            reference/#section/Glossary'>Glossary</a>). *(Use 'data_fields' to request this data.)*
        hr_zone_2 (Union[Unset, int]): Duration in seconds when heart rate was in an intense zone (cf. <a href='/api-
            reference/#section/Glossary'>Glossary</a>). *(Use 'data_fields' to request this data.)*
        hr_zone_3 (Union[Unset, int]): Duration in seconds when heart rate was in maximal zone (cf. <a href='/api-
            reference/#section/Glossary'>Glossary</a>). *(Use 'data_fields' to request this data.)*
        intense (Union[Unset, int]): Duration of intense activities (in seconds). *(Use 'data_fields' to request this
            data.)*
        is_tracker (Union[Unset, bool]): Is true if data was tracked by a Withings tracker (such as Pulse, Go and
            Watches) otherwise data was tracked by a mobile application or an external way
        moderate (Union[Unset, int]): Duration of moderate activities (in seconds). *(Use 'data_fields' to request this
            data.)*
        soft (Union[Unset, int]): Duration of soft activities (in seconds). *(Use 'data_fields' to request this data.)*
        steps (Union[Unset, int]): Number of steps. *(Use 'data_fields' to request this data.)*
        timezone (Union[Unset, str]): Timezone for the date.
        totalcalories (Union[Unset, float]): Total calories burned (in Kcal). Obtained by adding active calories (see
            ```calories```) and passive calories.
    """

    active: Union[Unset, int] = UNSET
    brand: Union[Unset, int] = UNSET
    calories: Union[Unset, float] = UNSET
    date: Union[Unset, str] = UNSET
    deviceid: Union[Unset, str] = UNSET
    distance: Union[Unset, float] = UNSET
    elevation: Union[Unset, float] = UNSET
    hash_deviceid: Union[Unset, str] = UNSET
    hr_average: Union[Unset, int] = UNSET
    hr_max: Union[Unset, int] = UNSET
    hr_min: Union[Unset, int] = UNSET
    hr_zone_0: Union[Unset, int] = UNSET
    hr_zone_1: Union[Unset, int] = UNSET
    hr_zone_2: Union[Unset, int] = UNSET
    hr_zone_3: Union[Unset, int] = UNSET
    intense: Union[Unset, int] = UNSET
    is_tracker: Union[Unset, bool] = UNSET
    moderate: Union[Unset, int] = UNSET
    soft: Union[Unset, int] = UNSET
    steps: Union[Unset, int] = UNSET
    timezone: Union[Unset, str] = UNSET
    totalcalories: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        brand = self.brand

        calories = self.calories

        date = self.date

        deviceid = self.deviceid

        distance = self.distance

        elevation = self.elevation

        hash_deviceid = self.hash_deviceid

        hr_average = self.hr_average

        hr_max = self.hr_max

        hr_min = self.hr_min

        hr_zone_0 = self.hr_zone_0

        hr_zone_1 = self.hr_zone_1

        hr_zone_2 = self.hr_zone_2

        hr_zone_3 = self.hr_zone_3

        intense = self.intense

        is_tracker = self.is_tracker

        moderate = self.moderate

        soft = self.soft

        steps = self.steps

        timezone = self.timezone

        totalcalories = self.totalcalories

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if brand is not UNSET:
            field_dict["brand"] = brand
        if calories is not UNSET:
            field_dict["calories"] = calories
        if date is not UNSET:
            field_dict["date"] = date
        if deviceid is not UNSET:
            field_dict["deviceid"] = deviceid
        if distance is not UNSET:
            field_dict["distance"] = distance
        if elevation is not UNSET:
            field_dict["elevation"] = elevation
        if hash_deviceid is not UNSET:
            field_dict["hash_deviceid"] = hash_deviceid
        if hr_average is not UNSET:
            field_dict["hr_average"] = hr_average
        if hr_max is not UNSET:
            field_dict["hr_max"] = hr_max
        if hr_min is not UNSET:
            field_dict["hr_min"] = hr_min
        if hr_zone_0 is not UNSET:
            field_dict["hr_zone_0"] = hr_zone_0
        if hr_zone_1 is not UNSET:
            field_dict["hr_zone_1"] = hr_zone_1
        if hr_zone_2 is not UNSET:
            field_dict["hr_zone_2"] = hr_zone_2
        if hr_zone_3 is not UNSET:
            field_dict["hr_zone_3"] = hr_zone_3
        if intense is not UNSET:
            field_dict["intense"] = intense
        if is_tracker is not UNSET:
            field_dict["is_tracker"] = is_tracker
        if moderate is not UNSET:
            field_dict["moderate"] = moderate
        if soft is not UNSET:
            field_dict["soft"] = soft
        if steps is not UNSET:
            field_dict["steps"] = steps
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if totalcalories is not UNSET:
            field_dict["totalcalories"] = totalcalories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        active = d.pop("active", UNSET)

        brand = d.pop("brand", UNSET)

        calories = d.pop("calories", UNSET)

        date = d.pop("date", UNSET)

        deviceid = d.pop("deviceid", UNSET)

        distance = d.pop("distance", UNSET)

        elevation = d.pop("elevation", UNSET)

        hash_deviceid = d.pop("hash_deviceid", UNSET)

        hr_average = d.pop("hr_average", UNSET)

        hr_max = d.pop("hr_max", UNSET)

        hr_min = d.pop("hr_min", UNSET)

        hr_zone_0 = d.pop("hr_zone_0", UNSET)

        hr_zone_1 = d.pop("hr_zone_1", UNSET)

        hr_zone_2 = d.pop("hr_zone_2", UNSET)

        hr_zone_3 = d.pop("hr_zone_3", UNSET)

        intense = d.pop("intense", UNSET)

        is_tracker = d.pop("is_tracker", UNSET)

        moderate = d.pop("moderate", UNSET)

        soft = d.pop("soft", UNSET)

        steps = d.pop("steps", UNSET)

        timezone = d.pop("timezone", UNSET)

        totalcalories = d.pop("totalcalories", UNSET)

        activity_object = cls(
            active=active,
            brand=brand,
            calories=calories,
            date=date,
            deviceid=deviceid,
            distance=distance,
            elevation=elevation,
            hash_deviceid=hash_deviceid,
            hr_average=hr_average,
            hr_max=hr_max,
            hr_min=hr_min,
            hr_zone_0=hr_zone_0,
            hr_zone_1=hr_zone_1,
            hr_zone_2=hr_zone_2,
            hr_zone_3=hr_zone_3,
            intense=intense,
            is_tracker=is_tracker,
            moderate=moderate,
            soft=soft,
            steps=steps,
            timezone=timezone,
            totalcalories=totalcalories,
        )

        activity_object.additional_properties = d
        return activity_object

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
