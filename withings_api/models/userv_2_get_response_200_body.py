from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.userv_2_get_response_200_body_user import Userv2GetResponse200BodyUser


T = TypeVar("T", bound="Userv2GetResponse200Body")


@_attrs_define
class Userv2GetResponse200Body:
    """Response data.

    Attributes:
        user (Union[Unset, Userv2GetResponse200BodyUser]):
    """

    user: Union[Unset, "Userv2GetResponse200BodyUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.userv_2_get_response_200_body_user import Userv2GetResponse200BodyUser

        d = src_dict.copy()
        _user = d.pop("user", UNSET)
        user: Union[Unset, Userv2GetResponse200BodyUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Userv2GetResponse200BodyUser.from_dict(_user)

        userv_2_get_response_200_body = cls(
            user=user,
        )

        userv_2_get_response_200_body.additional_properties = d
        return userv_2_get_response_200_body

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
