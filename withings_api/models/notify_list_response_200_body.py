from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notify_object import NotifyObject


T = TypeVar("T", bound="NotifyListResponse200Body")


@_attrs_define
class NotifyListResponse200Body:
    """Response data.

    Attributes:
        profiles (Union[Unset, list['NotifyObject']]): List of notification configurations for this user.
    """

    profiles: Union[Unset, list["NotifyObject"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profiles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.profiles, Unset):
            profiles = []
            for profiles_item_data in self.profiles:
                profiles_item = profiles_item_data.to_dict()
                profiles.append(profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profiles is not UNSET:
            field_dict["profiles"] = profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.notify_object import NotifyObject

        d = src_dict.copy()
        profiles = []
        _profiles = d.pop("profiles", UNSET)
        for profiles_item_data in _profiles or []:
            profiles_item = NotifyObject.from_dict(profiles_item_data)

            profiles.append(profiles_item)

        notify_list_response_200_body = cls(
            profiles=profiles,
        )

        notify_list_response_200_body.additional_properties = d
        return notify_list_response_200_body

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
