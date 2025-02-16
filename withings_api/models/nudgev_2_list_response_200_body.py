from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nudge import Nudge


T = TypeVar("T", bound="Nudgev2ListResponse200Body")


@_attrs_define
class Nudgev2ListResponse200Body:
    """Response data.

    Attributes:
        nudges (Union[Unset, list['Nudge']]):
    """

    nudges: Union[Unset, list["Nudge"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nudges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nudges, Unset):
            nudges = []
            for nudges_item_data in self.nudges:
                nudges_item = nudges_item_data.to_dict()
                nudges.append(nudges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nudges is not UNSET:
            field_dict["nudges"] = nudges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.nudge import Nudge

        d = src_dict.copy()
        nudges = []
        _nudges = d.pop("nudges", UNSET)
        for nudges_item_data in _nudges or []:
            nudges_item = Nudge.from_dict(nudges_item_data)

            nudges.append(nudges_item)

        nudgev_2_list_response_200_body = cls(
            nudges=nudges,
        )

        nudgev_2_list_response_200_body.additional_properties = d
        return nudgev_2_list_response_200_body

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
