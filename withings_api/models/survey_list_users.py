from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SurveyListUsers")


@_attrs_define
class SurveyListUsers:
    """
    Attributes:
        activation_date (Union[Unset, int]): Timestamp when the survey has been activated for the user
        userid (Union[Unset, int]): The id of the user.
    """

    activation_date: Union[Unset, int] = UNSET
    userid: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activation_date = self.activation_date

        userid = self.userid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activation_date is not UNSET:
            field_dict["activation_date"] = activation_date
        if userid is not UNSET:
            field_dict["userid"] = userid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        activation_date = d.pop("activation_date", UNSET)

        userid = d.pop("userid", UNSET)

        survey_list_users = cls(
            activation_date=activation_date,
            userid=userid,
        )

        survey_list_users.additional_properties = d
        return survey_list_users

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
