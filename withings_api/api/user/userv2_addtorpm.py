from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.userv_2_addtorpm_response_200 import Userv2AddtorpmResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    userid: int,
    programid: int,
    sms_onboarding: Union[Unset, bool] = UNSET,
    assistance_onboarding: Union[Unset, bool] = UNSET,
    icdcodeids: Union[Unset, str] = UNSET,
    external_ids: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["signature"] = signature

    params["client_id"] = client_id

    params["nonce"] = nonce

    params["userid"] = userid

    params["programid"] = programid

    params["sms_onboarding"] = sms_onboarding

    params["assistance_onboarding"] = assistance_onboarding

    params["icdcodeids"] = icdcodeids

    params["external_ids"] = external_ids

    params["category"] = category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/user",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Userv2AddtorpmResponse200]:
    if response.status_code == 200:
        response_200 = Userv2AddtorpmResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Userv2AddtorpmResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    userid: int,
    programid: int,
    sms_onboarding: Union[Unset, bool] = UNSET,
    assistance_onboarding: Union[Unset, bool] = UNSET,
    icdcodeids: Union[Unset, str] = UNSET,
    external_ids: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
) -> Response[Userv2AddtorpmResponse200]:
    """User v2  - Addtorpm

     This API allows you to add an existing user to the Withings Remote Patient Monitoring platform as a
    patient. Note: A Withings Remote Patient Monitoring contract is required to use this API.

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        userid (int):
        programid (int):
        sms_onboarding (Union[Unset, bool]):
        assistance_onboarding (Union[Unset, bool]):
        icdcodeids (Union[Unset, str]):
        external_ids (Union[Unset, str]):
        category (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Userv2AddtorpmResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        userid=userid,
        programid=programid,
        sms_onboarding=sms_onboarding,
        assistance_onboarding=assistance_onboarding,
        icdcodeids=icdcodeids,
        external_ids=external_ids,
        category=category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    userid: int,
    programid: int,
    sms_onboarding: Union[Unset, bool] = UNSET,
    assistance_onboarding: Union[Unset, bool] = UNSET,
    icdcodeids: Union[Unset, str] = UNSET,
    external_ids: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
) -> Optional[Userv2AddtorpmResponse200]:
    """User v2  - Addtorpm

     This API allows you to add an existing user to the Withings Remote Patient Monitoring platform as a
    patient. Note: A Withings Remote Patient Monitoring contract is required to use this API.

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        userid (int):
        programid (int):
        sms_onboarding (Union[Unset, bool]):
        assistance_onboarding (Union[Unset, bool]):
        icdcodeids (Union[Unset, str]):
        external_ids (Union[Unset, str]):
        category (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Userv2AddtorpmResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        userid=userid,
        programid=programid,
        sms_onboarding=sms_onboarding,
        assistance_onboarding=assistance_onboarding,
        icdcodeids=icdcodeids,
        external_ids=external_ids,
        category=category,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    userid: int,
    programid: int,
    sms_onboarding: Union[Unset, bool] = UNSET,
    assistance_onboarding: Union[Unset, bool] = UNSET,
    icdcodeids: Union[Unset, str] = UNSET,
    external_ids: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
) -> Response[Userv2AddtorpmResponse200]:
    """User v2  - Addtorpm

     This API allows you to add an existing user to the Withings Remote Patient Monitoring platform as a
    patient. Note: A Withings Remote Patient Monitoring contract is required to use this API.

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        userid (int):
        programid (int):
        sms_onboarding (Union[Unset, bool]):
        assistance_onboarding (Union[Unset, bool]):
        icdcodeids (Union[Unset, str]):
        external_ids (Union[Unset, str]):
        category (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Userv2AddtorpmResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        userid=userid,
        programid=programid,
        sms_onboarding=sms_onboarding,
        assistance_onboarding=assistance_onboarding,
        icdcodeids=icdcodeids,
        external_ids=external_ids,
        category=category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    userid: int,
    programid: int,
    sms_onboarding: Union[Unset, bool] = UNSET,
    assistance_onboarding: Union[Unset, bool] = UNSET,
    icdcodeids: Union[Unset, str] = UNSET,
    external_ids: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
) -> Optional[Userv2AddtorpmResponse200]:
    """User v2  - Addtorpm

     This API allows you to add an existing user to the Withings Remote Patient Monitoring platform as a
    patient. Note: A Withings Remote Patient Monitoring contract is required to use this API.

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        userid (int):
        programid (int):
        sms_onboarding (Union[Unset, bool]):
        assistance_onboarding (Union[Unset, bool]):
        icdcodeids (Union[Unset, str]):
        external_ids (Union[Unset, str]):
        category (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Userv2AddtorpmResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            signature=signature,
            client_id=client_id,
            nonce=nonce,
            userid=userid,
            programid=programid,
            sms_onboarding=sms_onboarding,
            assistance_onboarding=assistance_onboarding,
            icdcodeids=icdcodeids,
            external_ids=external_ids,
            category=category,
        )
    ).parsed
