from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nudgev_2_get_response_200_body_nudge import Nudgev2GetResponse200BodyNudge


T = TypeVar("T", bound="Nudgev2GetResponse200Body")


@_attrs_define
class Nudgev2GetResponse200Body:
    """Response data.

    Attributes:
        nudge (Union[Unset, Nudgev2GetResponse200BodyNudge]):
    """

    nudge: Union[Unset, "Nudgev2GetResponse200BodyNudge"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nudge: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.nudge, Unset):
            nudge = self.nudge.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nudge is not UNSET:
            field_dict["nudge"] = nudge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.nudgev_2_get_response_200_body_nudge import Nudgev2GetResponse200BodyNudge

        d = src_dict.copy()
        _nudge = d.pop("nudge", UNSET)
        nudge: Union[Unset, Nudgev2GetResponse200BodyNudge]
        if isinstance(_nudge, Unset):
            nudge = UNSET
        else:
            nudge = Nudgev2GetResponse200BodyNudge.from_dict(_nudge)

        nudgev_2_get_response_200_body = cls(
            nudge=nudge,
        )

        nudgev_2_get_response_200_body.additional_properties = d
        return nudgev_2_get_response_200_body

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
