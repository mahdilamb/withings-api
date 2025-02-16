from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dropshipment_get_order_status_object import DropshipmentGetOrderStatusObject


T = TypeVar("T", bound="Orderv2GetdetailResponse200Body")


@_attrs_define
class Orderv2GetdetailResponse200Body:
    """Response data.

    Attributes:
        orders (Union[Unset, list['DropshipmentGetOrderStatusObject']]):
    """

    orders: Union[Unset, list["DropshipmentGetOrderStatusObject"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        orders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orders is not UNSET:
            field_dict["orders"] = orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dropshipment_get_order_status_object import DropshipmentGetOrderStatusObject

        d = src_dict.copy()
        orders = []
        _orders = d.pop("orders", UNSET)
        for orders_item_data in _orders or []:
            orders_item = DropshipmentGetOrderStatusObject.from_dict(orders_item_data)

            orders.append(orders_item)

        orderv_2_getdetail_response_200_body = cls(
            orders=orders,
        )

        orderv_2_getdetail_response_200_body.additional_properties = d
        return orderv_2_getdetail_response_200_body

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
