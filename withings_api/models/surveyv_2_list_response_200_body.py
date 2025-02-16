from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.survey_list import SurveyList


T = TypeVar("T", bound="Surveyv2ListResponse200Body")


@_attrs_define
class Surveyv2ListResponse200Body:
    """Response data.

    Attributes:
        surveys (Union[Unset, list['SurveyList']]):
    """

    surveys: Union[Unset, list["SurveyList"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        surveys: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.surveys, Unset):
            surveys = []
            for surveys_item_data in self.surveys:
                surveys_item = surveys_item_data.to_dict()
                surveys.append(surveys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if surveys is not UNSET:
            field_dict["surveys"] = surveys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.survey_list import SurveyList

        d = src_dict.copy()
        surveys = []
        _surveys = d.pop("surveys", UNSET)
        for surveys_item_data in _surveys or []:
            surveys_item = SurveyList.from_dict(surveys_item_data)

            surveys.append(surveys_item)

        surveyv_2_list_response_200_body = cls(
            surveys=surveys,
        )

        surveyv_2_list_response_200_body.additional_properties = d
        return surveyv_2_list_response_200_body

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
