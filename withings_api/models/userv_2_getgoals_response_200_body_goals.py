from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.userv_2_getgoals_response_200_body_goals_weight import Userv2GetgoalsResponse200BodyGoalsWeight


T = TypeVar("T", bound="Userv2GetgoalsResponse200BodyGoals")


@_attrs_define
class Userv2GetgoalsResponse200BodyGoals:
    """
    Attributes:
        sleep (Union[Unset, int]): Sleep duration (in seconds). Example: 28800.
        steps (Union[Unset, int]): Number of steps per day. Example: 10000.
        weight (Union[Unset, Userv2GetgoalsResponse200BodyGoalsWeight]): Weight.
    """

    sleep: Union[Unset, int] = UNSET
    steps: Union[Unset, int] = UNSET
    weight: Union[Unset, "Userv2GetgoalsResponse200BodyGoalsWeight"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sleep = self.sleep

        steps = self.steps

        weight: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sleep is not UNSET:
            field_dict["sleep"] = sleep
        if steps is not UNSET:
            field_dict["steps"] = steps
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.userv_2_getgoals_response_200_body_goals_weight import Userv2GetgoalsResponse200BodyGoalsWeight

        d = src_dict.copy()
        sleep = d.pop("sleep", UNSET)

        steps = d.pop("steps", UNSET)

        _weight = d.pop("weight", UNSET)
        weight: Union[Unset, Userv2GetgoalsResponse200BodyGoalsWeight]
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = Userv2GetgoalsResponse200BodyGoalsWeight.from_dict(_weight)

        userv_2_getgoals_response_200_body_goals = cls(
            sleep=sleep,
            steps=steps,
            weight=weight,
        )

        userv_2_getgoals_response_200_body_goals.additional_properties = d
        return userv_2_getgoals_response_200_body_goals

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
