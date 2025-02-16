from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.answers_list_answers_item_type_1 import AnswersListAnswersItemType1


T = TypeVar("T", bound="AnswersList")


@_attrs_define
class AnswersList:
    """
    Attributes:
        answers (Union[Unset, list[Union['AnswersListAnswersItemType1', str]]]):
        grpid (Union[Unset, int]): Unique identifier of the measure group.
        surveyid (Union[Unset, int]):
        timestamp (Union[Unset, int]): Timestamp of the recording.
    """

    answers: Union[Unset, list[Union["AnswersListAnswersItemType1", str]]] = UNSET
    grpid: Union[Unset, int] = UNSET
    surveyid: Union[Unset, int] = UNSET
    timestamp: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.answers_list_answers_item_type_1 import AnswersListAnswersItemType1

        answers: Union[Unset, list[Union[dict[str, Any], str]]] = UNSET
        if not isinstance(self.answers, Unset):
            answers = []
            for answers_item_data in self.answers:
                answers_item: Union[dict[str, Any], str]
                if isinstance(answers_item_data, AnswersListAnswersItemType1):
                    answers_item = answers_item_data.to_dict()
                else:
                    answers_item = answers_item_data
                answers.append(answers_item)

        grpid = self.grpid

        surveyid = self.surveyid

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if answers is not UNSET:
            field_dict["answers"] = answers
        if grpid is not UNSET:
            field_dict["grpid"] = grpid
        if surveyid is not UNSET:
            field_dict["surveyid"] = surveyid
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.answers_list_answers_item_type_1 import AnswersListAnswersItemType1

        d = src_dict.copy()
        answers = []
        _answers = d.pop("answers", UNSET)
        for answers_item_data in _answers or []:

            def _parse_answers_item(data: object) -> Union["AnswersListAnswersItemType1", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    answers_item_type_1 = AnswersListAnswersItemType1.from_dict(data)

                    return answers_item_type_1
                except:  # noqa: E722
                    pass
                return cast(Union["AnswersListAnswersItemType1", str], data)

            answers_item = _parse_answers_item(answers_item_data)

            answers.append(answers_item)

        grpid = d.pop("grpid", UNSET)

        surveyid = d.pop("surveyid", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        answers_list = cls(
            answers=answers,
            grpid=grpid,
            surveyid=surveyid,
            timestamp=timestamp,
        )

        answers_list.additional_properties = d
        return answers_list

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
