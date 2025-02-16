from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Signaturev2GetnonceResponse200Body")


@_attrs_define
class Signaturev2GetnonceResponse200Body:
    """Response data.

    Attributes:
        nonce (Union[Unset, str]): A random timestamp based token to be used once in requiring signature API services to
            avoid replay attack Example: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d.
    """

    nonce: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nonce = self.nonce

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nonce is not UNSET:
            field_dict["nonce"] = nonce

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        nonce = d.pop("nonce", UNSET)

        signaturev_2_getnonce_response_200_body = cls(
            nonce=nonce,
        )

        signaturev_2_getnonce_response_200_body.additional_properties = d
        return signaturev_2_getnonce_response_200_body

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
