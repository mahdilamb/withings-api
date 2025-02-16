from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_object import ActivityObject


T = TypeVar("T", bound="Measurev2GetactivityResponse200Body")


@_attrs_define
class Measurev2GetactivityResponse200Body:
    """Response data.

    Attributes:
        activities (Union[Unset, list['ActivityObject']]):
        more (Union[Unset, bool]): To know if there is more data to fetch or not.
        offset (Union[Unset, int]): Offset to use to retrieve the next data.
    """

    activities: Union[Unset, list["ActivityObject"]] = UNSET
    more: Union[Unset, bool] = UNSET
    offset: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.activities, Unset):
            activities = []
            for activities_item_data in self.activities:
                activities_item = activities_item_data.to_dict()
                activities.append(activities_item)

        more = self.more

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activities is not UNSET:
            field_dict["activities"] = activities
        if more is not UNSET:
            field_dict["more"] = more
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.activity_object import ActivityObject

        d = src_dict.copy()
        activities = []
        _activities = d.pop("activities", UNSET)
        for activities_item_data in _activities or []:
            activities_item = ActivityObject.from_dict(activities_item_data)

            activities.append(activities_item)

        more = d.pop("more", UNSET)

        offset = d.pop("offset", UNSET)

        measurev_2_getactivity_response_200_body = cls(
            activities=activities,
            more=more,
            offset=offset,
        )

        measurev_2_getactivity_response_200_body.additional_properties = d
        return measurev_2_getactivity_response_200_body

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
