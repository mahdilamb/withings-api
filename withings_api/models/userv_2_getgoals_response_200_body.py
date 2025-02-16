from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.userv_2_getgoals_response_200_body_goals import Userv2GetgoalsResponse200BodyGoals


T = TypeVar("T", bound="Userv2GetgoalsResponse200Body")


@_attrs_define
class Userv2GetgoalsResponse200Body:
    """Response data.

    Attributes:
        goals (Union[Unset, Userv2GetgoalsResponse200BodyGoals]):
    """

    goals: Union[Unset, "Userv2GetgoalsResponse200BodyGoals"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goals: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.goals, Unset):
            goals = self.goals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if goals is not UNSET:
            field_dict["goals"] = goals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.userv_2_getgoals_response_200_body_goals import Userv2GetgoalsResponse200BodyGoals

        d = src_dict.copy()
        _goals = d.pop("goals", UNSET)
        goals: Union[Unset, Userv2GetgoalsResponse200BodyGoals]
        if isinstance(_goals, Unset):
            goals = UNSET
        else:
            goals = Userv2GetgoalsResponse200BodyGoals.from_dict(_goals)

        userv_2_getgoals_response_200_body = cls(
            goals=goals,
        )

        userv_2_getgoals_response_200_body.additional_properties = d
        return userv_2_getgoals_response_200_body

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
