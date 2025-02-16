from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Nudge")


@_attrs_define
class Nudge:
    """
    Attributes:
        campaignids (Union[Unset, list[int]]):
        content (Union[Unset, list[str]]):  Example: ['Line 1', 'Line 2'].
        created (Union[Unset, int]):
        iconids (Union[Unset, list[int]]):  Example: [3].
        model (Union[Unset, int]):
        modified (Union[Unset, int]): The timestamp of the last modification.
        position (Union[Unset, str]): The device's position during the measure.


            | Value | Description|
            |---|---|
            |0 | Right Wrist|
            |1 | Left Wrist|
            |2 | Right Arm|
            |3 | Left Arm|
            |4 | Right Foot|
            |5 | Left Foot|
            |6 | Between Legs|
            |8 | Left part of the body|
            |9 | Right part of the body|
            |10 | Left leg|
            |11 | Right leg|
            |12 | Torso|
            |13 | Left hand|
            |14 | Right hand|
    """

    campaignids: Union[Unset, list[int]] = UNSET
    content: Union[Unset, list[str]] = UNSET
    created: Union[Unset, int] = UNSET
    iconids: Union[Unset, list[int]] = UNSET
    model: Union[Unset, int] = UNSET
    modified: Union[Unset, int] = UNSET
    position: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaignids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.campaignids, Unset):
            campaignids = self.campaignids

        content: Union[Unset, list[str]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content

        created = self.created

        iconids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.iconids, Unset):
            iconids = self.iconids

        model = self.model

        modified = self.modified

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campaignids is not UNSET:
            field_dict["campaignids"] = campaignids
        if content is not UNSET:
            field_dict["content"] = content
        if created is not UNSET:
            field_dict["created"] = created
        if iconids is not UNSET:
            field_dict["iconids"] = iconids
        if model is not UNSET:
            field_dict["model"] = model
        if modified is not UNSET:
            field_dict["modified"] = modified
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        campaignids = cast(list[int], d.pop("campaignids", UNSET))

        content = cast(list[str], d.pop("content", UNSET))

        created = d.pop("created", UNSET)

        iconids = cast(list[int], d.pop("iconids", UNSET))

        model = d.pop("model", UNSET)

        modified = d.pop("modified", UNSET)

        position = d.pop("position", UNSET)

        nudge = cls(
            campaignids=campaignids,
            content=content,
            created=created,
            iconids=iconids,
            model=model,
            modified=modified,
            position=position,
        )

        nudge.additional_properties = d
        return nudge

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
