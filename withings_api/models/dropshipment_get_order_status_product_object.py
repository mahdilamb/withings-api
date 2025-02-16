from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dropshipment_get_order_status_product_device_object import (
        DropshipmentGetOrderStatusProductDeviceObject,
    )


T = TypeVar("T", bound="DropshipmentGetOrderStatusProductObject")


@_attrs_define
class DropshipmentGetOrderStatusProductObject:
    """
    Attributes:
        devices (Union[Unset, list['DropshipmentGetOrderStatusProductDeviceObject']]):
        ean (Union[Unset, str]): EAN of the product.
        mac_addresses (Union[Unset, list[str]]): List of device MAC addresses. *(Only if order has been shipped)*
            Example: ['00:24:e4:xx:xx:xx', '00:24:e4:xx:xx:xx', '00:24:e4:xx:xx:xx'].
        quantity (Union[Unset, int]): Quantity of products.
    """

    devices: Union[Unset, list["DropshipmentGetOrderStatusProductDeviceObject"]] = UNSET
    ean: Union[Unset, str] = UNSET
    mac_addresses: Union[Unset, list[str]] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        ean = self.ean

        mac_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.mac_addresses, Unset):
            mac_addresses = self.mac_addresses

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices
        if ean is not UNSET:
            field_dict["ean"] = ean
        if mac_addresses is not UNSET:
            field_dict["mac_addresses"] = mac_addresses
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dropshipment_get_order_status_product_device_object import (
            DropshipmentGetOrderStatusProductDeviceObject,
        )

        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = DropshipmentGetOrderStatusProductDeviceObject.from_dict(devices_item_data)

            devices.append(devices_item)

        ean = d.pop("ean", UNSET)

        mac_addresses = cast(list[str], d.pop("mac_addresses", UNSET))

        quantity = d.pop("quantity", UNSET)

        dropshipment_get_order_status_product_object = cls(
            devices=devices,
            ean=ean,
            mac_addresses=mac_addresses,
            quantity=quantity,
        )

        dropshipment_get_order_status_product_object.additional_properties = d
        return dropshipment_get_order_status_product_object

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
