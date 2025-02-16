from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.token_request_refresh_with_signature_grant_type import TokenRequestRefreshWithSignatureGrantType

T = TypeVar("T", bound="TokenRequestRefreshWithSignature")


@_attrs_define
class TokenRequestRefreshWithSignature:
    """
    Attributes:
        action (str): Must take the string value requesttoken.
        client_id (str): Your Client ID.
        grant_type (TokenRequestRefreshWithSignatureGrantType): Must take the constant string value refresh_token.
        nonce (str): A random token used to prevent replay attacks (Cf. Signature v2 - Getnonce).
        refresh_token (str): The current valid refresh_token.
        signature (str): Hash of params (Cf. Signature hash protocol).
    """

    action: str
    client_id: str
    grant_type: TokenRequestRefreshWithSignatureGrantType
    nonce: str
    refresh_token: str
    signature: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        client_id = self.client_id

        grant_type = self.grant_type.value

        nonce = self.nonce

        refresh_token = self.refresh_token

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "client_id": client_id,
                "grant_type": grant_type,
                "nonce": nonce,
                "refresh_token": refresh_token,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        action = d.pop("action")

        client_id = d.pop("client_id")

        grant_type = TokenRequestRefreshWithSignatureGrantType(d.pop("grant_type"))

        nonce = d.pop("nonce")

        refresh_token = d.pop("refresh_token")

        signature = d.pop("signature")

        token_request_refresh_with_signature = cls(
            action=action,
            client_id=client_id,
            grant_type=grant_type,
            nonce=nonce,
            refresh_token=refresh_token,
            signature=signature,
        )

        token_request_refresh_with_signature.additional_properties = d
        return token_request_refresh_with_signature

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
