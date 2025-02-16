from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nudge_campaign import NudgeCampaign


T = TypeVar("T", bound="Nudgecampaignv2ListResponse200Body")


@_attrs_define
class Nudgecampaignv2ListResponse200Body:
    """Response data.

    Attributes:
        campaigns (Union[Unset, list['NudgeCampaign']]):
    """

    campaigns: Union[Unset, list["NudgeCampaign"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaigns: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.campaigns, Unset):
            campaigns = []
            for campaigns_item_data in self.campaigns:
                campaigns_item = campaigns_item_data.to_dict()
                campaigns.append(campaigns_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campaigns is not UNSET:
            field_dict["campaigns"] = campaigns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.nudge_campaign import NudgeCampaign

        d = src_dict.copy()
        campaigns = []
        _campaigns = d.pop("campaigns", UNSET)
        for campaigns_item_data in _campaigns or []:
            campaigns_item = NudgeCampaign.from_dict(campaigns_item_data)

            campaigns.append(campaigns_item)

        nudgecampaignv_2_list_response_200_body = cls(
            campaigns=campaigns,
        )

        nudgecampaignv_2_list_response_200_body.additional_properties = d
        return nudgecampaignv_2_list_response_200_body

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
