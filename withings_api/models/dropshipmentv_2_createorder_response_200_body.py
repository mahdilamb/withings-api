from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dropshipment_create_order_object import DropshipmentCreateOrderObject


T = TypeVar("T", bound="Dropshipmentv2CreateorderResponse200Body")


@_attrs_define
class Dropshipmentv2CreateorderResponse200Body:
    """Response data.

    Attributes:
        dropshipmentorderid (Union[Unset, str]): Unique identifier of the dropshipment order. Example: 4874687.
        invalid_address_customer_ref_ids (Union[Unset, list[str]]): References of the orders with invalid address.
            *(Only if at least one order has an invalid address)*
        orders (Union[Unset, list['DropshipmentCreateOrderObject']]): List of created orders. *(Only if orders were
            successfully created)*
    """

    dropshipmentorderid: Union[Unset, str] = UNSET
    invalid_address_customer_ref_ids: Union[Unset, list[str]] = UNSET
    orders: Union[Unset, list["DropshipmentCreateOrderObject"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dropshipmentorderid = self.dropshipmentorderid

        invalid_address_customer_ref_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.invalid_address_customer_ref_ids, Unset):
            invalid_address_customer_ref_ids = self.invalid_address_customer_ref_ids

        orders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dropshipmentorderid is not UNSET:
            field_dict["dropshipmentorderid"] = dropshipmentorderid
        if invalid_address_customer_ref_ids is not UNSET:
            field_dict["invalid_address_customer_ref_ids"] = invalid_address_customer_ref_ids
        if orders is not UNSET:
            field_dict["orders"] = orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dropshipment_create_order_object import DropshipmentCreateOrderObject

        d = src_dict.copy()
        dropshipmentorderid = d.pop("dropshipmentorderid", UNSET)

        invalid_address_customer_ref_ids = cast(list[str], d.pop("invalid_address_customer_ref_ids", UNSET))

        orders = []
        _orders = d.pop("orders", UNSET)
        for orders_item_data in _orders or []:
            orders_item = DropshipmentCreateOrderObject.from_dict(orders_item_data)

            orders.append(orders_item)

        dropshipmentv_2_createorder_response_200_body = cls(
            dropshipmentorderid=dropshipmentorderid,
            invalid_address_customer_ref_ids=invalid_address_customer_ref_ids,
            orders=orders,
        )

        dropshipmentv_2_createorder_response_200_body.additional_properties = d
        return dropshipmentv_2_createorder_response_200_body

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
