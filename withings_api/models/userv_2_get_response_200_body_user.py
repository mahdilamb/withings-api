from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.userv_2_get_response_200_body_user_unit_pref import Userv2GetResponse200BodyUserUnitPref


T = TypeVar("T", bound="Userv2GetResponse200BodyUser")


@_attrs_define
class Userv2GetResponse200BodyUser:
    """
    Attributes:
        birthdate (Union[Unset, int]): Unix timestamp of user's birthdate Example: 1577829600.
        email (Union[Unset, str]): User's email address Example: john.doe@my.email.
        firstname (Union[Unset, str]): User's firstname Example: John.
        gender (Union[Unset, int]): User's gender (0: man, 1: woman)
        lastname (Union[Unset, str]): User's lastname Example: Doe.
        mailingpref (Union[Unset, bool]): User consent to receiving sales and marketing communication from Withings (0:
            user does not consent, 1: user does consent) Example: True.
        phonenumber (Union[Unset, str]): User's phone number. *(Only if set)* Example: +33612345678.
        preflang (Union[Unset, str]): User's language preference. Examples: en_EN / en_US / de_DE / es_ES / fr_FR /
            it_IT / ja_JA / ko_KR / nl_NL / pt_PT / ru_RU / zh_CN Example: fr_FR.
        shortname (Union[Unset, str]): User's shortname Example: JDO.
        timezone (Union[Unset, str]): User's timezone. Examples: "Europe/Paris" / "America/New_York". A complete list of
            all possible timezones can be found on the "TZ database name" column of this page :
            https://en.wikipedia.org/wiki/List_of_tz_database_time_zones Example: Europe/Paris.
        unit_pref (Union[Unset, Userv2GetResponse200BodyUserUnitPref]): User's unit preferences (cf. [Unit
            preferences](#tag/models/Unit-preferences) model).
    """

    birthdate: Union[Unset, int] = UNSET
    email: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    gender: Union[Unset, int] = UNSET
    lastname: Union[Unset, str] = UNSET
    mailingpref: Union[Unset, bool] = UNSET
    phonenumber: Union[Unset, str] = UNSET
    preflang: Union[Unset, str] = UNSET
    shortname: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    unit_pref: Union[Unset, "Userv2GetResponse200BodyUserUnitPref"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        birthdate = self.birthdate

        email = self.email

        firstname = self.firstname

        gender = self.gender

        lastname = self.lastname

        mailingpref = self.mailingpref

        phonenumber = self.phonenumber

        preflang = self.preflang

        shortname = self.shortname

        timezone = self.timezone

        unit_pref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.unit_pref, Unset):
            unit_pref = self.unit_pref.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if email is not UNSET:
            field_dict["email"] = email
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if gender is not UNSET:
            field_dict["gender"] = gender
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if mailingpref is not UNSET:
            field_dict["mailingpref"] = mailingpref
        if phonenumber is not UNSET:
            field_dict["phonenumber"] = phonenumber
        if preflang is not UNSET:
            field_dict["preflang"] = preflang
        if shortname is not UNSET:
            field_dict["shortname"] = shortname
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if unit_pref is not UNSET:
            field_dict["unit_pref"] = unit_pref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.userv_2_get_response_200_body_user_unit_pref import Userv2GetResponse200BodyUserUnitPref

        d = src_dict.copy()
        birthdate = d.pop("birthdate", UNSET)

        email = d.pop("email", UNSET)

        firstname = d.pop("firstname", UNSET)

        gender = d.pop("gender", UNSET)

        lastname = d.pop("lastname", UNSET)

        mailingpref = d.pop("mailingpref", UNSET)

        phonenumber = d.pop("phonenumber", UNSET)

        preflang = d.pop("preflang", UNSET)

        shortname = d.pop("shortname", UNSET)

        timezone = d.pop("timezone", UNSET)

        _unit_pref = d.pop("unit_pref", UNSET)
        unit_pref: Union[Unset, Userv2GetResponse200BodyUserUnitPref]
        if isinstance(_unit_pref, Unset):
            unit_pref = UNSET
        else:
            unit_pref = Userv2GetResponse200BodyUserUnitPref.from_dict(_unit_pref)

        userv_2_get_response_200_body_user = cls(
            birthdate=birthdate,
            email=email,
            firstname=firstname,
            gender=gender,
            lastname=lastname,
            mailingpref=mailingpref,
            phonenumber=phonenumber,
            preflang=preflang,
            shortname=shortname,
            timezone=timezone,
            unit_pref=unit_pref,
        )

        userv_2_get_response_200_body_user.additional_properties = d
        return userv_2_get_response_200_body_user

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
