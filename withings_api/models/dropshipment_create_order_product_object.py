from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DropshipmentCreateOrderProductObject")


@_attrs_define
class DropshipmentCreateOrderProductObject:
    """
    Attributes:
        ean (Union[Unset, str]): EAN of the product.
        quantity (Union[Unset, int]): Quantity of products.
    """

    ean: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ean = self.ean

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ean is not UNSET:
            field_dict["ean"] = ean
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ean = d.pop("ean", UNSET)

        quantity = d.pop("quantity", UNSET)

        dropshipment_create_order_product_object = cls(
            ean=ean,
            quantity=quantity,
        )

        dropshipment_create_order_product_object.additional_properties = d
        return dropshipment_create_order_product_object

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
