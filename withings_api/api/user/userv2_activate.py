from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.userv_2_activate_response_200 import Userv2ActivateResponse200
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
    mac_addresses: str,
    firstname: Union[Unset, str] = UNSET,
    lastname: Union[Unset, str] = UNSET,
    phonenumber: Union[Unset, str] = UNSET,
    recovery_code: Union[Unset, str] = UNSET,
    scope_oauth2: Union[Unset, str] = UNSET,
    goals: Union[Unset, str] = UNSET,
    password: Union[Unset, str] = UNSET,
    redirect_uri: Union[Unset, str] = UNSET,
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

    params["mac_addresses"] = mac_addresses

    params["firstname"] = firstname

    params["lastname"] = lastname

    params["phonenumber"] = phonenumber

    params["recovery_code"] = recovery_code

    params["scope_oauth2"] = scope_oauth2

    params["goals"] = goals

    params["password"] = password

    params["redirect_uri"] = redirect_uri

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/user",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Userv2ActivateResponse200]:
    if response.status_code == 200:
        response_200 = Userv2ActivateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Userv2ActivateResponse200]:
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
    mac_addresses: str,
    firstname: Union[Unset, str] = UNSET,
    lastname: Union[Unset, str] = UNSET,
    phonenumber: Union[Unset, str] = UNSET,
    recovery_code: Union[Unset, str] = UNSET,
    scope_oauth2: Union[Unset, str] = UNSET,
    goals: Union[Unset, str] = UNSET,
    password: Union[Unset, str] = UNSET,
    redirect_uri: Union[Unset, str] = UNSET,
) -> Response[Userv2ActivateResponse200]:
    """User v2  - Activate

     Creates a Withings user, links the devices related to the provided ```mac_addresses``` and activates
    the cellular devices service and invoicing.

    Please refer to the [Access and refresh tokens section](/developer-guide/v3/integration-
    guide/bulkship-cellular/get-access/access-and-refresh-tokens) to learn how to use the authorization
    code you'll get in return of this service in order to fetch user data. The authorization code is
    only valid for *10 minutes*.

    **Important**:

    - Please note that to activate the Withings HUB cellular service, the ```mac_address``` of the
    Withings HUB needs to be passed included in the input mac_addresses along with the other Withings
    devices.
    - Please note that the devices need to be authorized to be linked by API by the Partner. Please
    [contact Withings](mailto:partner-api@withings.com) for more information on device authorization.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*
    *Use this service only if you're integrating Withings Cellular Solutions with bulkshipment.*

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
        mac_addresses (str):
        firstname (Union[Unset, str]):
        lastname (Union[Unset, str]):
        phonenumber (Union[Unset, str]):
        recovery_code (Union[Unset, str]):
        scope_oauth2 (Union[Unset, str]):
        goals (Union[Unset, str]):
        password (Union[Unset, str]):
        redirect_uri (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Userv2ActivateResponse200]
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
        mac_addresses=mac_addresses,
        firstname=firstname,
        lastname=lastname,
        phonenumber=phonenumber,
        recovery_code=recovery_code,
        scope_oauth2=scope_oauth2,
        goals=goals,
        password=password,
        redirect_uri=redirect_uri,
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
    mac_addresses: str,
    firstname: Union[Unset, str] = UNSET,
    lastname: Union[Unset, str] = UNSET,
    phonenumber: Union[Unset, str] = UNSET,
    recovery_code: Union[Unset, str] = UNSET,
    scope_oauth2: Union[Unset, str] = UNSET,
    goals: Union[Unset, str] = UNSET,
    password: Union[Unset, str] = UNSET,
    redirect_uri: Union[Unset, str] = UNSET,
) -> Optional[Userv2ActivateResponse200]:
    """User v2  - Activate

     Creates a Withings user, links the devices related to the provided ```mac_addresses``` and activates
    the cellular devices service and invoicing.

    Please refer to the [Access and refresh tokens section](/developer-guide/v3/integration-
    guide/bulkship-cellular/get-access/access-and-refresh-tokens) to learn how to use the authorization
    code you'll get in return of this service in order to fetch user data. The authorization code is
    only valid for *10 minutes*.

    **Important**:

    - Please note that to activate the Withings HUB cellular service, the ```mac_address``` of the
    Withings HUB needs to be passed included in the input mac_addresses along with the other Withings
    devices.
    - Please note that the devices need to be authorized to be linked by API by the Partner. Please
    [contact Withings](mailto:partner-api@withings.com) for more information on device authorization.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*
    *Use this service only if you're integrating Withings Cellular Solutions with bulkshipment.*

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
        mac_addresses (str):
        firstname (Union[Unset, str]):
        lastname (Union[Unset, str]):
        phonenumber (Union[Unset, str]):
        recovery_code (Union[Unset, str]):
        scope_oauth2 (Union[Unset, str]):
        goals (Union[Unset, str]):
        password (Union[Unset, str]):
        redirect_uri (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Userv2ActivateResponse200
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
        mac_addresses=mac_addresses,
        firstname=firstname,
        lastname=lastname,
        phonenumber=phonenumber,
        recovery_code=recovery_code,
        scope_oauth2=scope_oauth2,
        goals=goals,
        password=password,
        redirect_uri=redirect_uri,
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
    mac_addresses: str,
    firstname: Union[Unset, str] = UNSET,
    lastname: Union[Unset, str] = UNSET,
    phonenumber: Union[Unset, str] = UNSET,
    recovery_code: Union[Unset, str] = UNSET,
    scope_oauth2: Union[Unset, str] = UNSET,
    goals: Union[Unset, str] = UNSET,
    password: Union[Unset, str] = UNSET,
    redirect_uri: Union[Unset, str] = UNSET,
) -> Response[Userv2ActivateResponse200]:
    """User v2  - Activate

     Creates a Withings user, links the devices related to the provided ```mac_addresses``` and activates
    the cellular devices service and invoicing.

    Please refer to the [Access and refresh tokens section](/developer-guide/v3/integration-
    guide/bulkship-cellular/get-access/access-and-refresh-tokens) to learn how to use the authorization
    code you'll get in return of this service in order to fetch user data. The authorization code is
    only valid for *10 minutes*.

    **Important**:

    - Please note that to activate the Withings HUB cellular service, the ```mac_address``` of the
    Withings HUB needs to be passed included in the input mac_addresses along with the other Withings
    devices.
    - Please note that the devices need to be authorized to be linked by API by the Partner. Please
    [contact Withings](mailto:partner-api@withings.com) for more information on device authorization.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*
    *Use this service only if you're integrating Withings Cellular Solutions with bulkshipment.*

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
        mac_addresses (str):
        firstname (Union[Unset, str]):
        lastname (Union[Unset, str]):
        phonenumber (Union[Unset, str]):
        recovery_code (Union[Unset, str]):
        scope_oauth2 (Union[Unset, str]):
        goals (Union[Unset, str]):
        password (Union[Unset, str]):
        redirect_uri (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Userv2ActivateResponse200]
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
        mac_addresses=mac_addresses,
        firstname=firstname,
        lastname=lastname,
        phonenumber=phonenumber,
        recovery_code=recovery_code,
        scope_oauth2=scope_oauth2,
        goals=goals,
        password=password,
        redirect_uri=redirect_uri,
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
    mac_addresses: str,
    firstname: Union[Unset, str] = UNSET,
    lastname: Union[Unset, str] = UNSET,
    phonenumber: Union[Unset, str] = UNSET,
    recovery_code: Union[Unset, str] = UNSET,
    scope_oauth2: Union[Unset, str] = UNSET,
    goals: Union[Unset, str] = UNSET,
    password: Union[Unset, str] = UNSET,
    redirect_uri: Union[Unset, str] = UNSET,
) -> Optional[Userv2ActivateResponse200]:
    """User v2  - Activate

     Creates a Withings user, links the devices related to the provided ```mac_addresses``` and activates
    the cellular devices service and invoicing.

    Please refer to the [Access and refresh tokens section](/developer-guide/v3/integration-
    guide/bulkship-cellular/get-access/access-and-refresh-tokens) to learn how to use the authorization
    code you'll get in return of this service in order to fetch user data. The authorization code is
    only valid for *10 minutes*.

    **Important**:

    - Please note that to activate the Withings HUB cellular service, the ```mac_address``` of the
    Withings HUB needs to be passed included in the input mac_addresses along with the other Withings
    devices.
    - Please note that the devices need to be authorized to be linked by API by the Partner. Please
    [contact Withings](mailto:partner-api@withings.com) for more information on device authorization.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*
    *Use this service only if you're integrating Withings Cellular Solutions with bulkshipment.*

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
        mac_addresses (str):
        firstname (Union[Unset, str]):
        lastname (Union[Unset, str]):
        phonenumber (Union[Unset, str]):
        recovery_code (Union[Unset, str]):
        scope_oauth2 (Union[Unset, str]):
        goals (Union[Unset, str]):
        password (Union[Unset, str]):
        redirect_uri (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Userv2ActivateResponse200
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
            mac_addresses=mac_addresses,
            firstname=firstname,
            lastname=lastname,
            phonenumber=phonenumber,
            recovery_code=recovery_code,
            scope_oauth2=scope_oauth2,
            goals=goals,
            password=password,
            redirect_uri=redirect_uri,
        )
    ).parsed
