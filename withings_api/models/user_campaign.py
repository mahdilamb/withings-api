from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserCampaign")


@_attrs_define
class UserCampaign:
    """
    Attributes:
        campaignid (Union[Unset, int]):
        completion_date (Union[Unset, int]):
        created (Union[Unset, int]):
        deliver_count (Union[Unset, int]):
        display_count (Union[Unset, int]):
        modified (Union[Unset, int]): The timestamp of the last modification.
        userid (Union[Unset, int]): The id of the user.
    """

    campaignid: Union[Unset, int] = UNSET
    completion_date: Union[Unset, int] = UNSET
    created: Union[Unset, int] = UNSET
    deliver_count: Union[Unset, int] = UNSET
    display_count: Union[Unset, int] = UNSET
    modified: Union[Unset, int] = UNSET
    userid: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaignid = self.campaignid

        completion_date = self.completion_date

        created = self.created

        deliver_count = self.deliver_count

        display_count = self.display_count

        modified = self.modified

        userid = self.userid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campaignid is not UNSET:
            field_dict["campaignid"] = campaignid
        if completion_date is not UNSET:
            field_dict["completion_date"] = completion_date
        if created is not UNSET:
            field_dict["created"] = created
        if deliver_count is not UNSET:
            field_dict["deliver_count"] = deliver_count
        if display_count is not UNSET:
            field_dict["display_count"] = display_count
        if modified is not UNSET:
            field_dict["modified"] = modified
        if userid is not UNSET:
            field_dict["userid"] = userid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        campaignid = d.pop("campaignid", UNSET)

        completion_date = d.pop("completion_date", UNSET)

        created = d.pop("created", UNSET)

        deliver_count = d.pop("deliver_count", UNSET)

        display_count = d.pop("display_count", UNSET)

        modified = d.pop("modified", UNSET)

        userid = d.pop("userid", UNSET)

        user_campaign = cls(
            campaignid=campaignid,
            completion_date=completion_date,
            created=created,
            deliver_count=deliver_count,
            display_count=display_count,
            modified=modified,
            userid=userid,
        )

        user_campaign.additional_properties = d
        return user_campaign

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
