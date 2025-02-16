from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.token_request_refresh_with_client_secret_grant_type import TokenRequestRefreshWithClientSecretGrantType

T = TypeVar("T", bound="TokenRequestRefreshWithClientSecret")


@_attrs_define
class TokenRequestRefreshWithClientSecret:
    """
    Attributes:
        action (str): Must take the string value requesttoken.
        client_id (str): Your Client ID.
        client_secret (str): Your Client Secret.
        grant_type (TokenRequestRefreshWithClientSecretGrantType): Must take the constant string value refresh_token.
        refresh_token (str): The current valid refresh_token.
    """

    action: str
    client_id: str
    client_secret: str
    grant_type: TokenRequestRefreshWithClientSecretGrantType
    refresh_token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        client_id = self.client_id

        client_secret = self.client_secret

        grant_type = self.grant_type.value

        refresh_token = self.refresh_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": grant_type,
                "refresh_token": refresh_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        action = d.pop("action")

        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        grant_type = TokenRequestRefreshWithClientSecretGrantType(d.pop("grant_type"))

        refresh_token = d.pop("refresh_token")

        token_request_refresh_with_client_secret = cls(
            action=action,
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            refresh_token=refresh_token,
        )

        token_request_refresh_with_client_secret.additional_properties = d
        return token_request_refresh_with_client_secret

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
