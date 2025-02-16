from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sleepv_2_get_response_200_body_series_hr import Sleepv2GetResponse200BodySeriesHr
    from ..models.sleepv_2_get_response_200_body_series_mvt_score import Sleepv2GetResponse200BodySeriesMvtScore
    from ..models.sleepv_2_get_response_200_body_series_rmssd import Sleepv2GetResponse200BodySeriesRmssd
    from ..models.sleepv_2_get_response_200_body_series_rr import Sleepv2GetResponse200BodySeriesRr
    from ..models.sleepv_2_get_response_200_body_series_sdnn_1 import Sleepv2GetResponse200BodySeriesSdnn1
    from ..models.sleepv_2_get_response_200_body_series_snoring import Sleepv2GetResponse200BodySeriesSnoring


T = TypeVar("T", bound="Sleepv2GetResponse200BodySeries")


@_attrs_define
class Sleepv2GetResponse200BodySeries:
    """
    Attributes:
        enddate (Union[Unset, int]): The end datetime for the sleep data. A single call can span up to 7 days maximum.
            To cover a wider time range, you will need to perform multiple calls. Example: 1594202400.
        hr (Union[Unset, Sleepv2GetResponse200BodySeriesHr]): Heart Rate. *(Use 'data_fields' to request this data.)*
        model (Union[Unset, str]): Device model. Value can be:


            | Value | Description|
            |---|---|
            |Aura Dock | Sleep Monitor|
            |Aura Sensor | Sleep Monitor|
            |Aura Sensor V2 | Sleep Monitor|
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
             Example: Aura Sensor V2.
        model_id (Union[Unset, int]):

            | Value | Description|
            |---|---|
            |60 | Aura Dock|
            |61 | Aura Sensor|
            |63 | Aura Sensor V2|
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
             Example: 63.
        mvt_score (Union[Unset, Sleepv2GetResponse200BodySeriesMvtScore]): Track the intensity of movement in bed on a
            minute-by-minute basis. Only available for EU devices and devices under prescription.
        rmssd (Union[Unset, Sleepv2GetResponse200BodySeriesRmssd]): Heart rate variability - Root mean square of the
            successive differences over "a few seconds"
        rr (Union[Unset, Sleepv2GetResponse200BodySeriesRr]): Respiration Rate. *(Use 'data_fields' to request this
            data.)*
        sdnn_1 (Union[Unset, Sleepv2GetResponse200BodySeriesSdnn1]): Heart rate variability - Standard deviation of the
            NN over 1 minute
        snoring (Union[Unset, Sleepv2GetResponse200BodySeriesSnoring]): Total snoring time
        startdate (Union[Unset, int]): The starting datetime for the sleep state data. Example: 1594159200.
        state (Union[Unset, int]): The state of sleeping. Values can be:


            | Value | Description|
            |---|---|
            |0 | Sleep state awake|
            |1 | Sleep state light|
            |2 | Sleep state deep|
            |3 | Sleep state rem|
            |4 | Sleep manual|
            |5 | Sleep unspecified|
             Example: 1.
    """

    enddate: Union[Unset, int] = UNSET
    hr: Union[Unset, "Sleepv2GetResponse200BodySeriesHr"] = UNSET
    model: Union[Unset, str] = UNSET
    model_id: Union[Unset, int] = UNSET
    mvt_score: Union[Unset, "Sleepv2GetResponse200BodySeriesMvtScore"] = UNSET
    rmssd: Union[Unset, "Sleepv2GetResponse200BodySeriesRmssd"] = UNSET
    rr: Union[Unset, "Sleepv2GetResponse200BodySeriesRr"] = UNSET
    sdnn_1: Union[Unset, "Sleepv2GetResponse200BodySeriesSdnn1"] = UNSET
    snoring: Union[Unset, "Sleepv2GetResponse200BodySeriesSnoring"] = UNSET
    startdate: Union[Unset, int] = UNSET
    state: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enddate = self.enddate

        hr: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hr, Unset):
            hr = self.hr.to_dict()

        model = self.model

        model_id = self.model_id

        mvt_score: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mvt_score, Unset):
            mvt_score = self.mvt_score.to_dict()

        rmssd: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rmssd, Unset):
            rmssd = self.rmssd.to_dict()

        rr: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rr, Unset):
            rr = self.rr.to_dict()

        sdnn_1: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sdnn_1, Unset):
            sdnn_1 = self.sdnn_1.to_dict()

        snoring: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.snoring, Unset):
            snoring = self.snoring.to_dict()

        startdate = self.startdate

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enddate is not UNSET:
            field_dict["enddate"] = enddate
        if hr is not UNSET:
            field_dict["hr"] = hr
        if model is not UNSET:
            field_dict["model"] = model
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if mvt_score is not UNSET:
            field_dict["mvt_score"] = mvt_score
        if rmssd is not UNSET:
            field_dict["rmssd"] = rmssd
        if rr is not UNSET:
            field_dict["rr"] = rr
        if sdnn_1 is not UNSET:
            field_dict["sdnn_1"] = sdnn_1
        if snoring is not UNSET:
            field_dict["snoring"] = snoring
        if startdate is not UNSET:
            field_dict["startdate"] = startdate
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sleepv_2_get_response_200_body_series_hr import Sleepv2GetResponse200BodySeriesHr
        from ..models.sleepv_2_get_response_200_body_series_mvt_score import Sleepv2GetResponse200BodySeriesMvtScore
        from ..models.sleepv_2_get_response_200_body_series_rmssd import Sleepv2GetResponse200BodySeriesRmssd
        from ..models.sleepv_2_get_response_200_body_series_rr import Sleepv2GetResponse200BodySeriesRr
        from ..models.sleepv_2_get_response_200_body_series_sdnn_1 import Sleepv2GetResponse200BodySeriesSdnn1
        from ..models.sleepv_2_get_response_200_body_series_snoring import Sleepv2GetResponse200BodySeriesSnoring

        d = src_dict.copy()
        enddate = d.pop("enddate", UNSET)

        _hr = d.pop("hr", UNSET)
        hr: Union[Unset, Sleepv2GetResponse200BodySeriesHr]
        if isinstance(_hr, Unset):
            hr = UNSET
        else:
            hr = Sleepv2GetResponse200BodySeriesHr.from_dict(_hr)

        model = d.pop("model", UNSET)

        model_id = d.pop("model_id", UNSET)

        _mvt_score = d.pop("mvt_score", UNSET)
        mvt_score: Union[Unset, Sleepv2GetResponse200BodySeriesMvtScore]
        if isinstance(_mvt_score, Unset):
            mvt_score = UNSET
        else:
            mvt_score = Sleepv2GetResponse200BodySeriesMvtScore.from_dict(_mvt_score)

        _rmssd = d.pop("rmssd", UNSET)
        rmssd: Union[Unset, Sleepv2GetResponse200BodySeriesRmssd]
        if isinstance(_rmssd, Unset):
            rmssd = UNSET
        else:
            rmssd = Sleepv2GetResponse200BodySeriesRmssd.from_dict(_rmssd)

        _rr = d.pop("rr", UNSET)
        rr: Union[Unset, Sleepv2GetResponse200BodySeriesRr]
        if isinstance(_rr, Unset):
            rr = UNSET
        else:
            rr = Sleepv2GetResponse200BodySeriesRr.from_dict(_rr)

        _sdnn_1 = d.pop("sdnn_1", UNSET)
        sdnn_1: Union[Unset, Sleepv2GetResponse200BodySeriesSdnn1]
        if isinstance(_sdnn_1, Unset):
            sdnn_1 = UNSET
        else:
            sdnn_1 = Sleepv2GetResponse200BodySeriesSdnn1.from_dict(_sdnn_1)

        _snoring = d.pop("snoring", UNSET)
        snoring: Union[Unset, Sleepv2GetResponse200BodySeriesSnoring]
        if isinstance(_snoring, Unset):
            snoring = UNSET
        else:
            snoring = Sleepv2GetResponse200BodySeriesSnoring.from_dict(_snoring)

        startdate = d.pop("startdate", UNSET)

        state = d.pop("state", UNSET)

        sleepv_2_get_response_200_body_series = cls(
            enddate=enddate,
            hr=hr,
            model=model,
            model_id=model_id,
            mvt_score=mvt_score,
            rmssd=rmssd,
            rr=rr,
            sdnn_1=sdnn_1,
            snoring=snoring,
            startdate=startdate,
            state=state,
        )

        sleepv_2_get_response_200_body_series.additional_properties = d
        return sleepv_2_get_response_200_body_series

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
