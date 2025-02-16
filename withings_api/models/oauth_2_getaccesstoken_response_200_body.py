from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Oauth2GetaccesstokenResponse200Body")


@_attrs_define
class Oauth2GetaccesstokenResponse200Body:
    """Response data.

    Attributes:
        access_token (Union[Unset, str]): Your new Access Token. Example: a075f8c14fb8df40b08ebc8508533dc332a6910a.
        csrf_token (Union[Unset, str]):  Example: PACnnxwHTaBQOzF7bQqwFUUotIuvtzSM.
        expires_in (Union[Unset, int]): Access token expiry delay in seconds. Example: 10800.
        refresh_token (Union[Unset, str]): Your Refresh Token. Example: f631236f02b991810feb774765b6ae8e6c6839ca.
        scope (Union[Unset, str]): You can get only the scope that the user accepted with the Token you have. Scopes can
            be 'user.info' 'user.metrics' 'user.activity' 'user.sleepevents'  and must be separated by a coma. Example:
            user.info,user.metrics.
        token_type (Union[Unset, str]): HTTP Authorization Header format: Bearer Example: Bearer.
        userid (Union[Unset, int]): The id of the user. Example: 363.
    """

    access_token: Union[Unset, str] = UNSET
    csrf_token: Union[Unset, str] = UNSET
    expires_in: Union[Unset, int] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    token_type: Union[Unset, str] = UNSET
    userid: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        csrf_token = self.csrf_token

        expires_in = self.expires_in

        refresh_token = self.refresh_token

        scope = self.scope

        token_type = self.token_type

        userid = self.userid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if csrf_token is not UNSET:
            field_dict["csrf_token"] = csrf_token
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if scope is not UNSET:
            field_dict["scope"] = scope
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if userid is not UNSET:
            field_dict["userid"] = userid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("access_token", UNSET)

        csrf_token = d.pop("csrf_token", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        scope = d.pop("scope", UNSET)

        token_type = d.pop("token_type", UNSET)

        userid = d.pop("userid", UNSET)

        oauth_2_getaccesstoken_response_200_body = cls(
            access_token=access_token,
            csrf_token=csrf_token,
            expires_in=expires_in,
            refresh_token=refresh_token,
            scope=scope,
            token_type=token_type,
            userid=userid,
        )

        oauth_2_getaccesstoken_response_200_body.additional_properties = d
        return oauth_2_getaccesstoken_response_200_body

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
