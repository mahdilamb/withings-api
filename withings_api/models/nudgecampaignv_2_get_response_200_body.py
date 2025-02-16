from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nudgecampaignv_2_get_response_200_body_campaign import Nudgecampaignv2GetResponse200BodyCampaign


T = TypeVar("T", bound="Nudgecampaignv2GetResponse200Body")


@_attrs_define
class Nudgecampaignv2GetResponse200Body:
    """Response data.

    Attributes:
        campaign (Union[Unset, Nudgecampaignv2GetResponse200BodyCampaign]):
    """

    campaign: Union[Unset, "Nudgecampaignv2GetResponse200BodyCampaign"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaign: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.campaign, Unset):
            campaign = self.campaign.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campaign is not UNSET:
            field_dict["campaign"] = campaign

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.nudgecampaignv_2_get_response_200_body_campaign import Nudgecampaignv2GetResponse200BodyCampaign

        d = src_dict.copy()
        _campaign = d.pop("campaign", UNSET)
        campaign: Union[Unset, Nudgecampaignv2GetResponse200BodyCampaign]
        if isinstance(_campaign, Unset):
            campaign = UNSET
        else:
            campaign = Nudgecampaignv2GetResponse200BodyCampaign.from_dict(_campaign)

        nudgecampaignv_2_get_response_200_body = cls(
            campaign=campaign,
        )

        nudgecampaignv_2_get_response_200_body.additional_properties = d
        return nudgecampaignv_2_get_response_200_body

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
