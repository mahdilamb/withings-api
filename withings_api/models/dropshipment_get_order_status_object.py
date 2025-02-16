from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dropshipment_get_order_status_product_object import DropshipmentGetOrderStatusProductObject


T = TypeVar("T", bound="DropshipmentGetOrderStatusObject")


@_attrs_define
class DropshipmentGetOrderStatusObject:
    """
    Attributes:
        carrier (Union[Unset, str]): Carrier. *(Only if order has been shipped)*
        carrier_service (Union[Unset, str]): Carrier service. *(Only if order has been shipped)*
        customer_ref_id (Union[Unset, str]): Random identifier you must provide in input parameters. It is used to track
            your order and must be unique.
        order_id (Union[Unset, str]): Withings generated identifier used to track your order.
        parcel_status (Union[Unset, str]): Status of the parcel. *(Only if order has been shipped)* Value can be:


            | Value|
            |---|
            |pending|
            |info_received|
            |in_transit|
            |failed_attempt|
            |exception|
            |delayed|
            |pickup|
            |delivered|
            |return|
            |expired|
        products (Union[Unset, list['DropshipmentGetOrderStatusProductObject']]):
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
        tracking_number (Union[Unset, str]): Tracking number. *(Only if order has been shipped)*
    """

    carrier: Union[Unset, str] = UNSET
    carrier_service: Union[Unset, str] = UNSET
    customer_ref_id: Union[Unset, str] = UNSET
    order_id: Union[Unset, str] = UNSET
    parcel_status: Union[Unset, str] = UNSET
    products: Union[Unset, list["DropshipmentGetOrderStatusProductObject"]] = UNSET
    status: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier = self.carrier

        carrier_service = self.carrier_service

        customer_ref_id = self.customer_ref_id

        order_id = self.order_id

        parcel_status = self.parcel_status

        products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        status = self.status

        tracking_number = self.tracking_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if carrier_service is not UNSET:
            field_dict["carrier_service"] = carrier_service
        if customer_ref_id is not UNSET:
            field_dict["customer_ref_id"] = customer_ref_id
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if parcel_status is not UNSET:
            field_dict["parcel_status"] = parcel_status
        if products is not UNSET:
            field_dict["products"] = products
        if status is not UNSET:
            field_dict["status"] = status
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dropshipment_get_order_status_product_object import DropshipmentGetOrderStatusProductObject

        d = src_dict.copy()
        carrier = d.pop("carrier", UNSET)

        carrier_service = d.pop("carrier_service", UNSET)

        customer_ref_id = d.pop("customer_ref_id", UNSET)

        order_id = d.pop("order_id", UNSET)

        parcel_status = d.pop("parcel_status", UNSET)

        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = DropshipmentGetOrderStatusProductObject.from_dict(products_item_data)

            products.append(products_item)

        status = d.pop("status", UNSET)

        tracking_number = d.pop("tracking_number", UNSET)

        dropshipment_get_order_status_object = cls(
            carrier=carrier,
            carrier_service=carrier_service,
            customer_ref_id=customer_ref_id,
            order_id=order_id,
            parcel_status=parcel_status,
            products=products,
            status=status,
            tracking_number=tracking_number,
        )

        dropshipment_get_order_status_object.additional_properties = d
        return dropshipment_get_order_status_object

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
