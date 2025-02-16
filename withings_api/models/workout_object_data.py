from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkoutObjectData")


@_attrs_define
class WorkoutObjectData:
    """Details of workout.

    Attributes:
        algo_pause_duration (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Total pause
            time in seconds detected by Withings device (swim only)
        calories (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Active calories burned
            (in Kcal). *(Use 'data_fields' to request this data.)*
        distance (Union[Unset, int]): *Available for all categories except Swimming, Multi-sport*<br><br>Distance
            travelled (in meters). *(Use 'data_fields' to request this data.)*
        elevation (Union[Unset, int]): *Available for all categories except Swimming, Multi-sport*<br><br>Number of
            floors climbed. *(Use 'data_fields' to request this data.)*
        hr_average (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Average heart rate.
            *(Use 'data_fields' to request this data.)*
        hr_max (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Maximal heart rate. *(Use
            'data_fields' to request this data.)*
        hr_min (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Minimal heart rate. *(Use
            'data_fields' to request this data.)*
        hr_zone_0 (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Duration in seconds when
            heart rate was in a light zone (cf. <a href='/api-reference/#section/Glossary'>Glossary</a>). *(Use
            'data_fields' to request this data.)*
        hr_zone_1 (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Duration in seconds when
            heart rate was in a moderate zone (cf. <a href='/api-reference/#section/Glossary'>Glossary</a>). *(Use
            'data_fields' to request this data.)*
        hr_zone_2 (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Duration in seconds when
            heart rate was in an intense zone (cf. <a href='/api-reference/#section/Glossary'>Glossary</a>). *(Use
            'data_fields' to request this data.)*
        hr_zone_3 (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Duration in seconds when
            heart rate was in maximal zone (cf. <a href='/api-reference/#section/Glossary'>Glossary</a>). *(Use
            'data_fields' to request this data.)*
        intensity (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Intensity of the
            workout, from 0 to 100, as inputed by the user. If the user didn't manually give the intensity of his workout,
            the value will be 0.
        manual_calories (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Active calories
            burned manually entered by user (in Kcal). *(Use 'data_fields' to request this data.)*
        manual_distance (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Distance travelled
            manually entered by user (in meters). *(Use 'data_fields' to request this data.)*
        pause_duration (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Total pause time in
            second filled by user
        pool_laps (Union[Unset, int]): *Available only for Swimming*<br><br>Number of pool laps. *(Use 'data_fields' to
            request this data.)*
        pool_length (Union[Unset, int]): *Available only for Swimming*<br><br>Length of the pool. *(Use 'data_fields' to
            request this data.)*
        spo2_average (Union[Unset, int]): *Available for all categories except Multi-sport*<br><br>Average percent of
            SpO2 percent value during a workout
        steps (Union[Unset, int]): *Available for all categories except Swimming, Multi-sport*<br><br>Number of steps.
            *(Use 'data_fields' to request this data.)*
        strokes (Union[Unset, int]): *Available only for Swimming*<br><br>Number of strokes. *(Use 'data_fields' to
            request this data.)*
    """

    algo_pause_duration: Union[Unset, int] = UNSET
    calories: Union[Unset, int] = UNSET
    distance: Union[Unset, int] = UNSET
    elevation: Union[Unset, int] = UNSET
    hr_average: Union[Unset, int] = UNSET
    hr_max: Union[Unset, int] = UNSET
    hr_min: Union[Unset, int] = UNSET
    hr_zone_0: Union[Unset, int] = UNSET
    hr_zone_1: Union[Unset, int] = UNSET
    hr_zone_2: Union[Unset, int] = UNSET
    hr_zone_3: Union[Unset, int] = UNSET
    intensity: Union[Unset, int] = UNSET
    manual_calories: Union[Unset, int] = UNSET
    manual_distance: Union[Unset, int] = UNSET
    pause_duration: Union[Unset, int] = UNSET
    pool_laps: Union[Unset, int] = UNSET
    pool_length: Union[Unset, int] = UNSET
    spo2_average: Union[Unset, int] = UNSET
    steps: Union[Unset, int] = UNSET
    strokes: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        algo_pause_duration = self.algo_pause_duration

        calories = self.calories

        distance = self.distance

        elevation = self.elevation

        hr_average = self.hr_average

        hr_max = self.hr_max

        hr_min = self.hr_min

        hr_zone_0 = self.hr_zone_0

        hr_zone_1 = self.hr_zone_1

        hr_zone_2 = self.hr_zone_2

        hr_zone_3 = self.hr_zone_3

        intensity = self.intensity

        manual_calories = self.manual_calories

        manual_distance = self.manual_distance

        pause_duration = self.pause_duration

        pool_laps = self.pool_laps

        pool_length = self.pool_length

        spo2_average = self.spo2_average

        steps = self.steps

        strokes = self.strokes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if algo_pause_duration is not UNSET:
            field_dict["algo_pause_duration"] = algo_pause_duration
        if calories is not UNSET:
            field_dict["calories"] = calories
        if distance is not UNSET:
            field_dict["distance"] = distance
        if elevation is not UNSET:
            field_dict["elevation"] = elevation
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
        if intensity is not UNSET:
            field_dict["intensity"] = intensity
        if manual_calories is not UNSET:
            field_dict["manual_calories"] = manual_calories
        if manual_distance is not UNSET:
            field_dict["manual_distance"] = manual_distance
        if pause_duration is not UNSET:
            field_dict["pause_duration"] = pause_duration
        if pool_laps is not UNSET:
            field_dict["pool_laps"] = pool_laps
        if pool_length is not UNSET:
            field_dict["pool_length"] = pool_length
        if spo2_average is not UNSET:
            field_dict["spo2_average"] = spo2_average
        if steps is not UNSET:
            field_dict["steps"] = steps
        if strokes is not UNSET:
            field_dict["strokes"] = strokes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        algo_pause_duration = d.pop("algo_pause_duration", UNSET)

        calories = d.pop("calories", UNSET)

        distance = d.pop("distance", UNSET)

        elevation = d.pop("elevation", UNSET)

        hr_average = d.pop("hr_average", UNSET)

        hr_max = d.pop("hr_max", UNSET)

        hr_min = d.pop("hr_min", UNSET)

        hr_zone_0 = d.pop("hr_zone_0", UNSET)

        hr_zone_1 = d.pop("hr_zone_1", UNSET)

        hr_zone_2 = d.pop("hr_zone_2", UNSET)

        hr_zone_3 = d.pop("hr_zone_3", UNSET)

        intensity = d.pop("intensity", UNSET)

        manual_calories = d.pop("manual_calories", UNSET)

        manual_distance = d.pop("manual_distance", UNSET)

        pause_duration = d.pop("pause_duration", UNSET)

        pool_laps = d.pop("pool_laps", UNSET)

        pool_length = d.pop("pool_length", UNSET)

        spo2_average = d.pop("spo2_average", UNSET)

        steps = d.pop("steps", UNSET)

        strokes = d.pop("strokes", UNSET)

        workout_object_data = cls(
            algo_pause_duration=algo_pause_duration,
            calories=calories,
            distance=distance,
            elevation=elevation,
            hr_average=hr_average,
            hr_max=hr_max,
            hr_min=hr_min,
            hr_zone_0=hr_zone_0,
            hr_zone_1=hr_zone_1,
            hr_zone_2=hr_zone_2,
            hr_zone_3=hr_zone_3,
            intensity=intensity,
            manual_calories=manual_calories,
            manual_distance=manual_distance,
            pause_duration=pause_duration,
            pool_laps=pool_laps,
            pool_length=pool_length,
            spo2_average=spo2_average,
            steps=steps,
            strokes=strokes,
        )

        workout_object_data.additional_properties = d
        return workout_object_data

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
