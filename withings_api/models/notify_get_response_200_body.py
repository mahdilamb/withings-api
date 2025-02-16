from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotifyGetResponse200Body")


@_attrs_define
class NotifyGetResponse200Body:
    """Response data.

    Attributes:
        appli (Union[Unset, int]): Refer to the [Notifications section](/developer-guide/v3/data-api/keep-user-data-up-
            to-date/) to know the meaning of each values.
             Example: 4.
        callbackurl (Union[Unset, str]): Callback url of the notification. Example: https://www.withings.com.
        comment (Union[Unset, str]): Comment entered when creating the notification configuration. Example: My
            notification subcription comment.
    """

    appli: Union[Unset, int] = UNSET
    callbackurl: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appli = self.appli

        callbackurl = self.callbackurl

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appli is not UNSET:
            field_dict["appli"] = appli
        if callbackurl is not UNSET:
            field_dict["callbackurl"] = callbackurl
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        appli = d.pop("appli", UNSET)

        callbackurl = d.pop("callbackurl", UNSET)

        comment = d.pop("comment", UNSET)

        notify_get_response_200_body = cls(
            appli=appli,
            callbackurl=callbackurl,
            comment=comment,
        )

        notify_get_response_200_body.additional_properties = d
        return notify_get_response_200_body

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
