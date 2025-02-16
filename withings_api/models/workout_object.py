from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workout_object_data import WorkoutObjectData


T = TypeVar("T", bound="WorkoutObject")


@_attrs_define
class WorkoutObject:
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
        category (Union[Unset, int]): Category of workout:


            | Value | Description|
            |---|---|
            |1 | Walk|
            |2 | Run|
            |3 | Hiking|
            |4 | Skating|
            |5 | BMX|
            |6 | Bicycling|
            |7 | Swimming|
            |8 | Surfing|
            |9 | Kitesurfing|
            |10 | Windsurfing|
            |11 | Bodyboard|
            |12 | Tennis|
            |13 | Table tennis|
            |14 | Squash|
            |15 | Badminton|
            |16 | Lift weights|
            |17 | Calisthenics|
            |18 | Elliptical|
            |19 | Pilates|
            |20 | Basket-ball|
            |21 | Soccer|
            |22 | Football|
            |23 | Rugby|
            |24 | Volley-ball|
            |25 | Waterpolo|
            |26 | Horse riding|
            |27 | Golf|
            |28 | Yoga|
            |29 | Dancing|
            |30 | Boxing|
            |31 | Fencing|
            |32 | Wrestling|
            |33 | Martial arts|
            |34 | Skiing|
            |35 | Snowboarding|
            |36 | Other|
            |128 | No activity|
            |187 | Rowing|
            |188 | Zumba|
            |191 | Baseball|
            |192 | Handball|
            |193 | Hockey|
            |194 | Ice hockey|
            |195 | Climbing|
            |196 | Ice skating|
            |272 | Multi-sport|
            |306 | Indoor walk|
            |307 | Indoor running|
            |308 | Indoor cycling|
        data (Union[Unset, WorkoutObjectData]): Details of workout.
        date (Union[Unset, str]): Date at which the measure was taken or entered.
        deviceid (Union[Unset, str]): ID of device that tracked the data. To retrieve information about this device,
            refer to : <a href='/api-reference/#operation/userv2-getdevice'>User v2 - Getdevice</a>.
        enddate (Union[Unset, int]): The ending datetime for workouts data.
        model (Union[Unset, int]): Source for the workout. Value can be:


            | Value | Description|
            |---|---|
            |1 | Withings WBS01, type: 1|
            |2 | Withings WBS03, type: 1|
            |3 | Kid Scale, type: 1|
            |4 | Withings WBS02, type: 1|
            |5 | Body+, type: 1|
            |6 | Body Cardio, type: 1|
            |7 | Body, type: 1|
            |13 | Body+, type: 1|
            |21 | Smart Baby Monitor, type: 2|
            |22 | Withings Home, type: 2|
            |41 | Withings Blood Pressure V1, type: 4|
            |42 | Withings Blood Pressure V2, type: 4|
            |43 | Withings Blood Pressure V3, type: 4|
            |44 | BPM Core, type: 4|
            |45 | BPM Connect, type: 4|
            |51 | Pulse, type: 16|
            |52 | Activite, type: 16|
            |53 | Activite (Pop, Steel), type: 16|
            |54 | Withings Go, type: 16|
            |55 | Activite Steel HR, type: 16|
            |58 | Pulse HR, type: 16|
            |59 | Activite Steel HR Sport Edition, type: 16|
            |60 | Aura dock, type: 32|
            |61 | Aura sensor, type: 32|
            |62 | Aura dock, type: 32|
            |63 | Sleep sensor, type: 32|
            |70 | Thermo, type: 64|
            |91 | Move ECG|
            |92 | Move ECG|
            |1051 | iOS step tracker, type 16|
            |1052 | iOS step tracker, type 16|
            |1053 | Android step tracker, type 16|
            |1054 | Android step tracker, type 16|
            |1055 | GoogleFit tracker, type 16|
            |1056 | Samsung Health tracker, type 16|
            |1057 | HealthKit step iPhone tracker, type 16|
            |1058 | HealthKit step Apple Watch tracker, type 16|
            |1059 | HealthKit other step tracker, type 16|
            |1060 | Android step tracker, type 16|
            |1062 | Huawei tracker, type 16|
        modified (Union[Unset, int]): The timestamp of the last modification.
        startdate (Union[Unset, int]): The starting datetime for workouts data.
        timezone (Union[Unset, str]): Timezone for the date.
    """

    attrib: Union[Unset, int] = UNSET
    category: Union[Unset, int] = UNSET
    data: Union[Unset, "WorkoutObjectData"] = UNSET
    date: Union[Unset, str] = UNSET
    deviceid: Union[Unset, str] = UNSET
    enddate: Union[Unset, int] = UNSET
    model: Union[Unset, int] = UNSET
    modified: Union[Unset, int] = UNSET
    startdate: Union[Unset, int] = UNSET
    timezone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attrib = self.attrib

        category = self.category

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        date = self.date

        deviceid = self.deviceid

        enddate = self.enddate

        model = self.model

        modified = self.modified

        startdate = self.startdate

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attrib is not UNSET:
            field_dict["attrib"] = attrib
        if category is not UNSET:
            field_dict["category"] = category
        if data is not UNSET:
            field_dict["data"] = data
        if date is not UNSET:
            field_dict["date"] = date
        if deviceid is not UNSET:
            field_dict["deviceid"] = deviceid
        if enddate is not UNSET:
            field_dict["enddate"] = enddate
        if model is not UNSET:
            field_dict["model"] = model
        if modified is not UNSET:
            field_dict["modified"] = modified
        if startdate is not UNSET:
            field_dict["startdate"] = startdate
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.workout_object_data import WorkoutObjectData

        d = src_dict.copy()
        attrib = d.pop("attrib", UNSET)

        category = d.pop("category", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, WorkoutObjectData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WorkoutObjectData.from_dict(_data)

        date = d.pop("date", UNSET)

        deviceid = d.pop("deviceid", UNSET)

        enddate = d.pop("enddate", UNSET)

        model = d.pop("model", UNSET)

        modified = d.pop("modified", UNSET)

        startdate = d.pop("startdate", UNSET)

        timezone = d.pop("timezone", UNSET)

        workout_object = cls(
            attrib=attrib,
            category=category,
            data=data,
            date=date,
            deviceid=deviceid,
            enddate=enddate,
            model=model,
            modified=modified,
            startdate=startdate,
            timezone=timezone,
        )

        workout_object.additional_properties = d
        return workout_object

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
