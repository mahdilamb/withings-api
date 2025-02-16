from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.token_request_with_client_secret_grant_type import TokenRequestWithClientSecretGrantType

T = TypeVar("T", bound="TokenRequestWithClientSecret")


@_attrs_define
class TokenRequestWithClientSecret:
    """
    Attributes:
        action (str): Must take the string value requesttoken.
        client_id (str): Your Client ID.
        client_secret (str): Your Client Secret.
        code (str): The Authorization Code you got from previous step.
        grant_type (TokenRequestWithClientSecretGrantType): Must take the constant string value authorization_code.
        redirect_uri (str): The URI you use in the first call.
    """

    action: str
    client_id: str
    client_secret: str
    code: str
    grant_type: TokenRequestWithClientSecretGrantType
    redirect_uri: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        client_id = self.client_id

        client_secret = self.client_secret

        code = self.code

        grant_type = self.grant_type.value

        redirect_uri = self.redirect_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "grant_type": grant_type,
                "redirect_uri": redirect_uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        action = d.pop("action")

        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        code = d.pop("code")

        grant_type = TokenRequestWithClientSecretGrantType(d.pop("grant_type"))

        redirect_uri = d.pop("redirect_uri")

        token_request_with_client_secret = cls(
            action=action,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            grant_type=grant_type,
            redirect_uri=redirect_uri,
        )

        token_request_with_client_secret.additional_properties = d
        return token_request_with_client_secret

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
