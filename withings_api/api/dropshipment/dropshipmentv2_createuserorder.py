from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dropshipmentv_2_createuserorder_response_200 import Dropshipmentv2CreateuserorderResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    client_id: str,
    nonce: str,
    signature: str,
    mailingpref: bool,
    birthdate: int,
    measures: str,
    gender: int,
    preflang: str,
    unit_pref: str,
    email: str,
    timezone: str,
    shortname: str,
    external_id: str,
    order: str,
    firstname: Union[Unset, str] = UNSET,
    lastname: Union[Unset, str] = UNSET,
    phonenumber: Union[Unset, str] = UNSET,
    recovery_code: Union[Unset, str] = UNSET,
    goals: Union[Unset, str] = UNSET,
    testmode: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["client_id"] = client_id

    params["nonce"] = nonce

    params["signature"] = signature

    params["mailingpref"] = mailingpref

    params["birthdate"] = birthdate

    params["measures"] = measures

    params["gender"] = gender

    params["preflang"] = preflang

    params["unit_pref"] = unit_pref

    params["email"] = email

    params["timezone"] = timezone

    params["shortname"] = shortname

    params["external_id"] = external_id

    params["order"] = order

    params["firstname"] = firstname

    params["lastname"] = lastname

    params["phonenumber"] = phonenumber

    params["recovery_code"] = recovery_code

    params["goals"] = goals

    params["testmode"] = testmode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/dropshipment",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Dropshipmentv2CreateuserorderResponse200]:
    if response.status_code == 200:
        response_200 = Dropshipmentv2CreateuserorderResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Dropshipmentv2CreateuserorderResponse200]:
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
    client_id: str,
    nonce: str,
    signature: str,
    mailingpref: bool,
    birthdate: int,
    measures: str,
    gender: int,
    preflang: str,
    unit_pref: str,
    email: str,
    timezone: str,
    shortname: str,
    external_id: str,
    order: str,
    firstname: Union[Unset, str] = UNSET,
    lastname: Union[Unset, str] = UNSET,
    phonenumber: Union[Unset, str] = UNSET,
    recovery_code: Union[Unset, str] = UNSET,
    goals: Union[Unset, str] = UNSET,
    testmode: Union[Unset, int] = UNSET,
) -> Response[Dropshipmentv2CreateuserorderResponse200]:
    """Dropshipment v2  - Createuserorder

     Creates a Withings user, then creates a dropshipment order and links the devices shipped to the
    created user once the device is shipped. If a cellular device is listed in the order field, the
    service will activate this device's cellular service and invoicing.

    If one of the orders has an invalid address, none of the orders will be created.

    Please refer to the [Access and refresh tokens section](/developer-guide/v3/integration-
    guide/dropship-cellular/get-access/access-and-refresh-tokens) to learn how to use the authorization
    code you'll get in return of this service in order to fetch user data. The authorization code is
    only valid for *10 minutes*.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*
    *Use this service only if you're integrating Withings Cellular Solutions with dropshipment.*

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        mailingpref (bool):
        birthdate (int):
        measures (str):
        gender (int):
        preflang (str):
        unit_pref (str):
        email (str):
        timezone (str):
        shortname (str):
        external_id (str):
        order (str):
        firstname (Union[Unset, str]):
        lastname (Union[Unset, str]):
        phonenumber (Union[Unset, str]):
        recovery_code (Union[Unset, str]):
        goals (Union[Unset, str]):
        testmode (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dropshipmentv2CreateuserorderResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        nonce=nonce,
        signature=signature,
        mailingpref=mailingpref,
        birthdate=birthdate,
        measures=measures,
        gender=gender,
        preflang=preflang,
        unit_pref=unit_pref,
        email=email,
        timezone=timezone,
        shortname=shortname,
        external_id=external_id,
        order=order,
        firstname=firstname,
        lastname=lastname,
        phonenumber=phonenumber,
        recovery_code=recovery_code,
        goals=goals,
        testmode=testmode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    nonce: str,
    signature: str,
    mailingpref: bool,
    birthdate: int,
    measures: str,
    gender: int,
    preflang: str,
    unit_pref: str,
    email: str,
    timezone: str,
    shortname: str,
    external_id: str,
    order: str,
    firstname: Union[Unset, str] = UNSET,
    lastname: Union[Unset, str] = UNSET,
    phonenumber: Union[Unset, str] = UNSET,
    recovery_code: Union[Unset, str] = UNSET,
    goals: Union[Unset, str] = UNSET,
    testmode: Union[Unset, int] = UNSET,
) -> Optional[Dropshipmentv2CreateuserorderResponse200]:
    """Dropshipment v2  - Createuserorder

     Creates a Withings user, then creates a dropshipment order and links the devices shipped to the
    created user once the device is shipped. If a cellular device is listed in the order field, the
    service will activate this device's cellular service and invoicing.

    If one of the orders has an invalid address, none of the orders will be created.

    Please refer to the [Access and refresh tokens section](/developer-guide/v3/integration-
    guide/dropship-cellular/get-access/access-and-refresh-tokens) to learn how to use the authorization
    code you'll get in return of this service in order to fetch user data. The authorization code is
    only valid for *10 minutes*.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*
    *Use this service only if you're integrating Withings Cellular Solutions with dropshipment.*

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        mailingpref (bool):
        birthdate (int):
        measures (str):
        gender (int):
        preflang (str):
        unit_pref (str):
        email (str):
        timezone (str):
        shortname (str):
        external_id (str):
        order (str):
        firstname (Union[Unset, str]):
        lastname (Union[Unset, str]):
        phonenumber (Union[Unset, str]):
        recovery_code (Union[Unset, str]):
        goals (Union[Unset, str]):
        testmode (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dropshipmentv2CreateuserorderResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        client_id=client_id,
        nonce=nonce,
        signature=signature,
        mailingpref=mailingpref,
        birthdate=birthdate,
        measures=measures,
        gender=gender,
        preflang=preflang,
        unit_pref=unit_pref,
        email=email,
        timezone=timezone,
        shortname=shortname,
        external_id=external_id,
        order=order,
        firstname=firstname,
        lastname=lastname,
        phonenumber=phonenumber,
        recovery_code=recovery_code,
        goals=goals,
        testmode=testmode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    nonce: str,
    signature: str,
    mailingpref: bool,
    birthdate: int,
    measures: str,
    gender: int,
    preflang: str,
    unit_pref: str,
    email: str,
    timezone: str,
    shortname: str,
    external_id: str,
    order: str,
    firstname: Union[Unset, str] = UNSET,
    lastname: Union[Unset, str] = UNSET,
    phonenumber: Union[Unset, str] = UNSET,
    recovery_code: Union[Unset, str] = UNSET,
    goals: Union[Unset, str] = UNSET,
    testmode: Union[Unset, int] = UNSET,
) -> Response[Dropshipmentv2CreateuserorderResponse200]:
    """Dropshipment v2  - Createuserorder

     Creates a Withings user, then creates a dropshipment order and links the devices shipped to the
    created user once the device is shipped. If a cellular device is listed in the order field, the
    service will activate this device's cellular service and invoicing.

    If one of the orders has an invalid address, none of the orders will be created.

    Please refer to the [Access and refresh tokens section](/developer-guide/v3/integration-
    guide/dropship-cellular/get-access/access-and-refresh-tokens) to learn how to use the authorization
    code you'll get in return of this service in order to fetch user data. The authorization code is
    only valid for *10 minutes*.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*
    *Use this service only if you're integrating Withings Cellular Solutions with dropshipment.*

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        mailingpref (bool):
        birthdate (int):
        measures (str):
        gender (int):
        preflang (str):
        unit_pref (str):
        email (str):
        timezone (str):
        shortname (str):
        external_id (str):
        order (str):
        firstname (Union[Unset, str]):
        lastname (Union[Unset, str]):
        phonenumber (Union[Unset, str]):
        recovery_code (Union[Unset, str]):
        goals (Union[Unset, str]):
        testmode (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dropshipmentv2CreateuserorderResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        nonce=nonce,
        signature=signature,
        mailingpref=mailingpref,
        birthdate=birthdate,
        measures=measures,
        gender=gender,
        preflang=preflang,
        unit_pref=unit_pref,
        email=email,
        timezone=timezone,
        shortname=shortname,
        external_id=external_id,
        order=order,
        firstname=firstname,
        lastname=lastname,
        phonenumber=phonenumber,
        recovery_code=recovery_code,
        goals=goals,
        testmode=testmode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    nonce: str,
    signature: str,
    mailingpref: bool,
    birthdate: int,
    measures: str,
    gender: int,
    preflang: str,
    unit_pref: str,
    email: str,
    timezone: str,
    shortname: str,
    external_id: str,
    order: str,
    firstname: Union[Unset, str] = UNSET,
    lastname: Union[Unset, str] = UNSET,
    phonenumber: Union[Unset, str] = UNSET,
    recovery_code: Union[Unset, str] = UNSET,
    goals: Union[Unset, str] = UNSET,
    testmode: Union[Unset, int] = UNSET,
) -> Optional[Dropshipmentv2CreateuserorderResponse200]:
    """Dropshipment v2  - Createuserorder

     Creates a Withings user, then creates a dropshipment order and links the devices shipped to the
    created user once the device is shipped. If a cellular device is listed in the order field, the
    service will activate this device's cellular service and invoicing.

    If one of the orders has an invalid address, none of the orders will be created.

    Please refer to the [Access and refresh tokens section](/developer-guide/v3/integration-
    guide/dropship-cellular/get-access/access-and-refresh-tokens) to learn how to use the authorization
    code you'll get in return of this service in order to fetch user data. The authorization code is
    only valid for *10 minutes*.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*
    *Use this service only if you're integrating Withings Cellular Solutions with dropshipment.*

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        mailingpref (bool):
        birthdate (int):
        measures (str):
        gender (int):
        preflang (str):
        unit_pref (str):
        email (str):
        timezone (str):
        shortname (str):
        external_id (str):
        order (str):
        firstname (Union[Unset, str]):
        lastname (Union[Unset, str]):
        phonenumber (Union[Unset, str]):
        recovery_code (Union[Unset, str]):
        goals (Union[Unset, str]):
        testmode (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dropshipmentv2CreateuserorderResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            client_id=client_id,
            nonce=nonce,
            signature=signature,
            mailingpref=mailingpref,
            birthdate=birthdate,
            measures=measures,
            gender=gender,
            preflang=preflang,
            unit_pref=unit_pref,
            email=email,
            timezone=timezone,
            shortname=shortname,
            external_id=external_id,
            order=order,
            firstname=firstname,
            lastname=lastname,
            phonenumber=phonenumber,
            recovery_code=recovery_code,
            goals=goals,
            testmode=testmode,
        )
    ).parsed
