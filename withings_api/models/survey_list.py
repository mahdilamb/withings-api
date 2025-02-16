from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.survey_list_trigger_conditions_item_type_1 import SurveyListTriggerConditionsItemType1


T = TypeVar("T", bound="SurveyList")


@_attrs_define
class SurveyList:
    """
    Attributes:
        answers_type (Union[Unset, int]):
        category (Union[Unset, int]):
        description (Union[Unset, str]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        trigger_conditions (Union[Unset, list[Union['SurveyListTriggerConditionsItemType1', str]]]):
        trigger_type (Union[Unset, int]):
    """

    answers_type: Union[Unset, int] = UNSET
    category: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    trigger_conditions: Union[Unset, list[Union["SurveyListTriggerConditionsItemType1", str]]] = UNSET
    trigger_type: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.survey_list_trigger_conditions_item_type_1 import SurveyListTriggerConditionsItemType1

        answers_type = self.answers_type

        category = self.category

        description = self.description

        id = self.id

        name = self.name

        trigger_conditions: Union[Unset, list[Union[dict[str, Any], str]]] = UNSET
        if not isinstance(self.trigger_conditions, Unset):
            trigger_conditions = []
            for trigger_conditions_item_data in self.trigger_conditions:
                trigger_conditions_item: Union[dict[str, Any], str]
                if isinstance(trigger_conditions_item_data, SurveyListTriggerConditionsItemType1):
                    trigger_conditions_item = trigger_conditions_item_data.to_dict()
                else:
                    trigger_conditions_item = trigger_conditions_item_data
                trigger_conditions.append(trigger_conditions_item)

        trigger_type = self.trigger_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if answers_type is not UNSET:
            field_dict["answers_type"] = answers_type
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if trigger_conditions is not UNSET:
            field_dict["trigger_conditions"] = trigger_conditions
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.survey_list_trigger_conditions_item_type_1 import SurveyListTriggerConditionsItemType1

        d = src_dict.copy()
        answers_type = d.pop("answers_type", UNSET)

        category = d.pop("category", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        trigger_conditions = []
        _trigger_conditions = d.pop("trigger_conditions", UNSET)
        for trigger_conditions_item_data in _trigger_conditions or []:

            def _parse_trigger_conditions_item(data: object) -> Union["SurveyListTriggerConditionsItemType1", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    trigger_conditions_item_type_1 = SurveyListTriggerConditionsItemType1.from_dict(data)

                    return trigger_conditions_item_type_1
                except:  # noqa: E722
                    pass
                return cast(Union["SurveyListTriggerConditionsItemType1", str], data)

            trigger_conditions_item = _parse_trigger_conditions_item(trigger_conditions_item_data)

            trigger_conditions.append(trigger_conditions_item)

        trigger_type = d.pop("trigger_type", UNSET)

        survey_list = cls(
            answers_type=answers_type,
            category=category,
            description=description,
            id=id,
            name=name,
            trigger_conditions=trigger_conditions,
            trigger_type=trigger_type,
        )

        survey_list.additional_properties = d
        return survey_list

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
