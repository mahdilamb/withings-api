from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dropshipment_create_order_product_object import DropshipmentCreateOrderProductObject


T = TypeVar("T", bound="DropshipmentCreateOrderObject")


@_attrs_define
class DropshipmentCreateOrderObject:
    """
    Attributes:
        customer_ref_id (Union[Unset, str]): Random identifier you must provide in input parameters. It is used to track
            your order and must be unique.
        dropshipmentorderid (Union[Unset, str]): Unique identifier of the dropshipment order.
        order_id (Union[Unset, str]): Withings generated identifier used to track your order.
        products (Union[Unset, list['DropshipmentCreateOrderProductObject']]):
        status (Union[Unset, str]): Status of the order. Value can be:


            | Value|
            |---|
            |CREATED|
            |ADDRESS VERIFICATION|
            |ADDRESS ERROR|
            |VERIFIED|
            |PROCESSING|
            |FAILED|
            |OPEN|
            |SHIPPED|
            |TRASHED|
            |BACKHOLD|
    """

    customer_ref_id: Union[Unset, str] = UNSET
    dropshipmentorderid: Union[Unset, str] = UNSET
    order_id: Union[Unset, str] = UNSET
    products: Union[Unset, list["DropshipmentCreateOrderProductObject"]] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_ref_id = self.customer_ref_id

        dropshipmentorderid = self.dropshipmentorderid

        order_id = self.order_id

        products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_ref_id is not UNSET:
            field_dict["customer_ref_id"] = customer_ref_id
        if dropshipmentorderid is not UNSET:
            field_dict["dropshipmentorderid"] = dropshipmentorderid
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if products is not UNSET:
            field_dict["products"] = products
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dropshipment_create_order_product_object import DropshipmentCreateOrderProductObject

        d = src_dict.copy()
        customer_ref_id = d.pop("customer_ref_id", UNSET)

        dropshipmentorderid = d.pop("dropshipmentorderid", UNSET)

        order_id = d.pop("order_id", UNSET)

        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = DropshipmentCreateOrderProductObject.from_dict(products_item_data)

            products.append(products_item)

        status = d.pop("status", UNSET)

        dropshipment_create_order_object = cls(
            customer_ref_id=customer_ref_id,
            dropshipmentorderid=dropshipmentorderid,
            order_id=order_id,
            products=products,
            status=status,
        )

        dropshipment_create_order_object.additional_properties = d
        return dropshipment_create_order_object

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
