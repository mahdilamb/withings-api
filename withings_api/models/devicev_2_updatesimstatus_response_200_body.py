from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Devicev2UpdatesimstatusResponse200Body")


@_attrs_define
class Devicev2UpdatesimstatusResponse200Body:
    """Response data.

    Attributes:
        new_sim_status (Union[Unset, str]): New status of the SIM. Example: STANDBY.
        termination_date (Union[Unset, int]): Timestamp when the SIM will be terminated *(Only if required status was
            ```TERMINATED```)* Example: 1656518088.
    """

    new_sim_status: Union[Unset, str] = UNSET
    termination_date: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_sim_status = self.new_sim_status

        termination_date = self.termination_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_sim_status is not UNSET:
            field_dict["new_sim_status"] = new_sim_status
        if termination_date is not UNSET:
            field_dict["termination_date"] = termination_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        new_sim_status = d.pop("new_sim_status", UNSET)

        termination_date = d.pop("termination_date", UNSET)

        devicev_2_updatesimstatus_response_200_body = cls(
            new_sim_status=new_sim_status,
            termination_date=termination_date,
        )

        devicev_2_updatesimstatus_response_200_body.additional_properties = d
        return devicev_2_updatesimstatus_response_200_body

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
