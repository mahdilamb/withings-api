from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.userv_2_addtorpm_response_200_body_program import Userv2AddtorpmResponse200BodyProgram
    from ..models.userv_2_addtorpm_response_200_body_user import Userv2AddtorpmResponse200BodyUser


T = TypeVar("T", bound="Userv2AddtorpmResponse200Body")


@_attrs_define
class Userv2AddtorpmResponse200Body:
    """Response data.

    Attributes:
        program (Union[Unset, Userv2AddtorpmResponse200BodyProgram]):
        user (Union[Unset, Userv2AddtorpmResponse200BodyUser]):
    """

    program: Union[Unset, "Userv2AddtorpmResponse200BodyProgram"] = UNSET
    user: Union[Unset, "Userv2AddtorpmResponse200BodyUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if program is not UNSET:
            field_dict["program"] = program
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.userv_2_addtorpm_response_200_body_program import Userv2AddtorpmResponse200BodyProgram
        from ..models.userv_2_addtorpm_response_200_body_user import Userv2AddtorpmResponse200BodyUser

        d = src_dict.copy()
        _program = d.pop("program", UNSET)
        program: Union[Unset, Userv2AddtorpmResponse200BodyProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = Userv2AddtorpmResponse200BodyProgram.from_dict(_program)

        _user = d.pop("user", UNSET)
        user: Union[Unset, Userv2AddtorpmResponse200BodyUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Userv2AddtorpmResponse200BodyUser.from_dict(_user)

        userv_2_addtorpm_response_200_body = cls(
            program=program,
            user=user,
        )

        userv_2_addtorpm_response_200_body.additional_properties = d
        return userv_2_addtorpm_response_200_body

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
