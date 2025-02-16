from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.token_request_with_signature_grant_type import TokenRequestWithSignatureGrantType

T = TypeVar("T", bound="TokenRequestWithSignature")


@_attrs_define
class TokenRequestWithSignature:
    """
    Attributes:
        action (str): Must take the string value requesttoken.
        client_id (str): Your Client ID.
        code (str): The Authorization Code you got from previous step.
        grant_type (TokenRequestWithSignatureGrantType): Must take the constant string value authorization_code.
        nonce (str): A random token used to prevent replay attacks (Cf. Signature v2 - Getnonce).
        redirect_uri (str): The URI you use in the first call.
        signature (str): Hash of params (Cf. Signature hash protocol).
    """

    action: str
    client_id: str
    code: str
    grant_type: TokenRequestWithSignatureGrantType
    nonce: str
    redirect_uri: str
    signature: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        client_id = self.client_id

        code = self.code

        grant_type = self.grant_type.value

        nonce = self.nonce

        redirect_uri = self.redirect_uri

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "client_id": client_id,
                "code": code,
                "grant_type": grant_type,
                "nonce": nonce,
                "redirect_uri": redirect_uri,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        action = d.pop("action")

        client_id = d.pop("client_id")

        code = d.pop("code")

        grant_type = TokenRequestWithSignatureGrantType(d.pop("grant_type"))

        nonce = d.pop("nonce")

        redirect_uri = d.pop("redirect_uri")

        signature = d.pop("signature")

        token_request_with_signature = cls(
            action=action,
            client_id=client_id,
            code=code,
            grant_type=grant_type,
            nonce=nonce,
            redirect_uri=redirect_uri,
            signature=signature,
        )

        token_request_with_signature.additional_properties = d
        return token_request_with_signature

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
