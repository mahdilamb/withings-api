from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_add_to_rpm_external_ids import UserAddToRpmExternalIds
    from ..models.userv_2_addtorpm_response_200_body_user_height import Userv2AddtorpmResponse200BodyUserHeight


T = TypeVar("T", bound="Userv2AddtorpmResponse200BodyUser")


@_attrs_define
class Userv2AddtorpmResponse200BodyUser:
    """
    Attributes:
        assistance_onboarding (Union[Unset, bool]):  Example: True.
        category (Union[Unset, int]):  Example: -6.
        device_models (Union[Unset, list[int]]):  Example: [765,15].
        device_types (Union[Unset, list[int]]):  Example: [1231,5675].
        external_ids (Union[Unset, list['UserAddToRpmExternalIds']]):
        height (Union[Unset, Userv2AddtorpmResponse200BodyUserHeight]):
        icd_codes (Union[Unset, list[int]]):  Example: [66,455].
        preflang (Union[Unset, str]): User's language preference. Examples: en_EN / en_US / de_DE / es_ES / fr_FR /
            it_IT / ja_JA / ko_KR / nl_NL / pt_PT / ru_RU / zh_CN Example: fr_FR.
        sms_notification (Union[Unset, bool]):  Example: True.
        sms_onboarding (Union[Unset, bool]):  Example: True.
        sms_reminder (Union[Unset, bool]):  Example: True.
    """

    assistance_onboarding: Union[Unset, bool] = UNSET
    category: Union[Unset, int] = UNSET
    device_models: Union[Unset, list[int]] = UNSET
    device_types: Union[Unset, list[int]] = UNSET
    external_ids: Union[Unset, list["UserAddToRpmExternalIds"]] = UNSET
    height: Union[Unset, "Userv2AddtorpmResponse200BodyUserHeight"] = UNSET
    icd_codes: Union[Unset, list[int]] = UNSET
    preflang: Union[Unset, str] = UNSET
    sms_notification: Union[Unset, bool] = UNSET
    sms_onboarding: Union[Unset, bool] = UNSET
    sms_reminder: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistance_onboarding = self.assistance_onboarding

        category = self.category

        device_models: Union[Unset, list[int]] = UNSET
        if not isinstance(self.device_models, Unset):
            device_models = self.device_models

        device_types: Union[Unset, list[int]] = UNSET
        if not isinstance(self.device_types, Unset):
            device_types = self.device_types

        external_ids: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_ids, Unset):
            external_ids = []
            for external_ids_item_data in self.external_ids:
                external_ids_item = external_ids_item_data.to_dict()
                external_ids.append(external_ids_item)

        height: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.height, Unset):
            height = self.height.to_dict()

        icd_codes: Union[Unset, list[int]] = UNSET
        if not isinstance(self.icd_codes, Unset):
            icd_codes = self.icd_codes

        preflang = self.preflang

        sms_notification = self.sms_notification

        sms_onboarding = self.sms_onboarding

        sms_reminder = self.sms_reminder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assistance_onboarding is not UNSET:
            field_dict["assistance_onboarding"] = assistance_onboarding
        if category is not UNSET:
            field_dict["category"] = category
        if device_models is not UNSET:
            field_dict["device_models"] = device_models
        if device_types is not UNSET:
            field_dict["device_types"] = device_types
        if external_ids is not UNSET:
            field_dict["external_ids"] = external_ids
        if height is not UNSET:
            field_dict["height"] = height
        if icd_codes is not UNSET:
            field_dict["icd_codes"] = icd_codes
        if preflang is not UNSET:
            field_dict["preflang"] = preflang
        if sms_notification is not UNSET:
            field_dict["sms_notification"] = sms_notification
        if sms_onboarding is not UNSET:
            field_dict["sms_onboarding"] = sms_onboarding
        if sms_reminder is not UNSET:
            field_dict["sms_reminder"] = sms_reminder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.user_add_to_rpm_external_ids import UserAddToRpmExternalIds
        from ..models.userv_2_addtorpm_response_200_body_user_height import Userv2AddtorpmResponse200BodyUserHeight

        d = src_dict.copy()
        assistance_onboarding = d.pop("assistance_onboarding", UNSET)

        category = d.pop("category", UNSET)

        device_models = cast(list[int], d.pop("device_models", UNSET))

        device_types = cast(list[int], d.pop("device_types", UNSET))

        external_ids = []
        _external_ids = d.pop("external_ids", UNSET)
        for external_ids_item_data in _external_ids or []:
            external_ids_item = UserAddToRpmExternalIds.from_dict(external_ids_item_data)

            external_ids.append(external_ids_item)

        _height = d.pop("height", UNSET)
        height: Union[Unset, Userv2AddtorpmResponse200BodyUserHeight]
        if isinstance(_height, Unset):
            height = UNSET
        else:
            height = Userv2AddtorpmResponse200BodyUserHeight.from_dict(_height)

        icd_codes = cast(list[int], d.pop("icd_codes", UNSET))

        preflang = d.pop("preflang", UNSET)

        sms_notification = d.pop("sms_notification", UNSET)

        sms_onboarding = d.pop("sms_onboarding", UNSET)

        sms_reminder = d.pop("sms_reminder", UNSET)

        userv_2_addtorpm_response_200_body_user = cls(
            assistance_onboarding=assistance_onboarding,
            category=category,
            device_models=device_models,
            device_types=device_types,
            external_ids=external_ids,
            height=height,
            icd_codes=icd_codes,
            preflang=preflang,
            sms_notification=sms_notification,
            sms_onboarding=sms_onboarding,
            sms_reminder=sms_reminder,
        )

        userv_2_addtorpm_response_200_body_user.additional_properties = d
        return userv_2_addtorpm_response_200_body_user

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
