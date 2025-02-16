from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Nudgecampaignv2CreateResponse200Body")


@_attrs_define
class Nudgecampaignv2CreateResponse200Body:
    """Response data.

    Attributes:
        campaignid (Union[Unset, int]):  Example: 9.
    """

    campaignid: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaignid = self.campaignid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campaignid is not UNSET:
            field_dict["campaignid"] = campaignid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        campaignid = d.pop("campaignid", UNSET)

        nudgecampaignv_2_create_response_200_body = cls(
            campaignid=campaignid,
        )

        nudgecampaignv_2_create_response_200_body.additional_properties = d
        return nudgecampaignv_2_create_response_200_body

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
