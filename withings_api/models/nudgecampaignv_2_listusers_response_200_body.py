from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_campaign import UserCampaign


T = TypeVar("T", bound="Nudgecampaignv2ListusersResponse200Body")


@_attrs_define
class Nudgecampaignv2ListusersResponse200Body:
    """Response data.

    Attributes:
        users (Union[Unset, list['UserCampaign']]):
    """

    users: Union[Unset, list["UserCampaign"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.user_campaign import UserCampaign

        d = src_dict.copy()
        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = UserCampaign.from_dict(users_item_data)

            users.append(users_item)

        nudgecampaignv_2_listusers_response_200_body = cls(
            users=users,
        )

        nudgecampaignv_2_listusers_response_200_body.additional_properties = d
        return nudgecampaignv_2_listusers_response_200_body

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
