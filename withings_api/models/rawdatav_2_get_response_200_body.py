from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rawdata_get_rawdata_object import RawdataGetRawdataObject


T = TypeVar("T", bound="Rawdatav2GetResponse200Body")


@_attrs_define
class Rawdatav2GetResponse200Body:
    """Response data.

    Attributes:
        more (Union[Unset, bool]): To know if there is more data to fetch or not.
        offset (Union[Unset, int]): Offset to use to retrieve the next data.
        rawdata (Union[Unset, list['RawdataGetRawdataObject']]):
    """

    more: Union[Unset, bool] = UNSET
    offset: Union[Unset, int] = UNSET
    rawdata: Union[Unset, list["RawdataGetRawdataObject"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        more = self.more

        offset = self.offset

        rawdata: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rawdata, Unset):
            rawdata = []
            for rawdata_item_data in self.rawdata:
                rawdata_item = rawdata_item_data.to_dict()
                rawdata.append(rawdata_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if more is not UNSET:
            field_dict["more"] = more
        if offset is not UNSET:
            field_dict["offset"] = offset
        if rawdata is not UNSET:
            field_dict["rawdata"] = rawdata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rawdata_get_rawdata_object import RawdataGetRawdataObject

        d = src_dict.copy()
        more = d.pop("more", UNSET)

        offset = d.pop("offset", UNSET)

        rawdata = []
        _rawdata = d.pop("rawdata", UNSET)
        for rawdata_item_data in _rawdata or []:
            rawdata_item = RawdataGetRawdataObject.from_dict(rawdata_item_data)

            rawdata.append(rawdata_item)

        rawdatav_2_get_response_200_body = cls(
            more=more,
            offset=offset,
            rawdata=rawdata,
        )

        rawdatav_2_get_response_200_body.additional_properties = d
        return rawdatav_2_get_response_200_body

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
