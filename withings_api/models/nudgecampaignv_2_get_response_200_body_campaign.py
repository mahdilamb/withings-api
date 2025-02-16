from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Nudgecampaignv2GetResponse200BodyCampaign")


@_attrs_define
class Nudgecampaignv2GetResponse200BodyCampaign:
    """
    Attributes:
        created (Union[Unset, int]):  Example: 1712016369.
        enddate (Union[Unset, int]): The end datetime for the sleep data. A single call can span up to 7 days maximum.
            To cover a wider time range, you will need to perform multiple calls. Example: 1735689600.
        id (Union[Unset, int]):  Example: 3.
        max_display_count (Union[Unset, int]):  Example: 5.
        modified (Union[Unset, int]): The timestamp of the last modification. Example: 1712016369.
        nudgeid (Union[Unset, int]):  Example: 4.
        startdate (Union[Unset, int]): The starting datetime for the sleep state data. Example: 1712106335.
        user_count (Union[Unset, int]):  Example: 2.
    """

    created: Union[Unset, int] = UNSET
    enddate: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    max_display_count: Union[Unset, int] = UNSET
    modified: Union[Unset, int] = UNSET
    nudgeid: Union[Unset, int] = UNSET
    startdate: Union[Unset, int] = UNSET
    user_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        enddate = self.enddate

        id = self.id

        max_display_count = self.max_display_count

        modified = self.modified

        nudgeid = self.nudgeid

        startdate = self.startdate

        user_count = self.user_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if enddate is not UNSET:
            field_dict["enddate"] = enddate
        if id is not UNSET:
            field_dict["id"] = id
        if max_display_count is not UNSET:
            field_dict["max_display_count"] = max_display_count
        if modified is not UNSET:
            field_dict["modified"] = modified
        if nudgeid is not UNSET:
            field_dict["nudgeid"] = nudgeid
        if startdate is not UNSET:
            field_dict["startdate"] = startdate
        if user_count is not UNSET:
            field_dict["user_count"] = user_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        created = d.pop("created", UNSET)

        enddate = d.pop("enddate", UNSET)

        id = d.pop("id", UNSET)

        max_display_count = d.pop("max_display_count", UNSET)

        modified = d.pop("modified", UNSET)

        nudgeid = d.pop("nudgeid", UNSET)

        startdate = d.pop("startdate", UNSET)

        user_count = d.pop("user_count", UNSET)

        nudgecampaignv_2_get_response_200_body_campaign = cls(
            created=created,
            enddate=enddate,
            id=id,
            max_display_count=max_display_count,
            modified=modified,
            nudgeid=nudgeid,
            startdate=startdate,
            user_count=user_count,
        )

        nudgecampaignv_2_get_response_200_body_campaign.additional_properties = d
        return nudgecampaignv_2_get_response_200_body_campaign

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
