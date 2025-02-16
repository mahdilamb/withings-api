from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.devicev_2_updatesimstatus_response_200_body import Devicev2UpdatesimstatusResponse200Body


T = TypeVar("T", bound="Devicev2UpdatesimstatusResponse200")


@_attrs_define
class Devicev2UpdatesimstatusResponse200:
    """
    Attributes:
        body (Union[Unset, Devicev2UpdatesimstatusResponse200Body]): Response data.
        status (Union[Unset, int]): Response status. See <a href='#section/Response-status'>Status</a> section for
            details.
    """

    body: Union[Unset, "Devicev2UpdatesimstatusResponse200Body"] = UNSET
    status: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.devicev_2_updatesimstatus_response_200_body import Devicev2UpdatesimstatusResponse200Body

        d = src_dict.copy()
        _body = d.pop("body", UNSET)
        body: Union[Unset, Devicev2UpdatesimstatusResponse200Body]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = Devicev2UpdatesimstatusResponse200Body.from_dict(_body)

        status = d.pop("status", UNSET)

        devicev_2_updatesimstatus_response_200 = cls(
            body=body,
            status=status,
        )

        devicev_2_updatesimstatus_response_200.additional_properties = d
        return devicev_2_updatesimstatus_response_200

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
