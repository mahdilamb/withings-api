from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Userv2ActivateResponse200BodyUser")


@_attrs_define
class Userv2ActivateResponse200BodyUser:
    """
    Attributes:
        code (Union[Unset, str]): Authorization Code that must be used to retrieve access_token and refresh_token. (Read
            the "Get access to your user's data" section of your [integration guide](/developer-guide/v3/withings-
            solutions/integration-guides) to learn more about how to get this parameter.) Example:
            490ed603fe9bd2ce10027bdba0c932069cd27085.
        external_id (Union[Unset, str]): Unique identifier used by partner to identify the end-user. Example:
            3b7a6db0-ec7e-479b-9675-2a3d8d6a7e51.
    """

    code: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        external_id = d.pop("external_id", UNSET)

        userv_2_activate_response_200_body_user = cls(
            code=code,
            external_id=external_id,
        )

        userv_2_activate_response_200_body_user.additional_properties = d
        return userv_2_activate_response_200_body_user

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
