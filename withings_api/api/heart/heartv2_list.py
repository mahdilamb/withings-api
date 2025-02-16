from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.heartv_2_list_response_200 import Heartv2ListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    startdate: Union[Unset, int] = UNSET,
    enddate: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["startdate"] = startdate

    params["enddate"] = enddate

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/heart",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Heartv2ListResponse200]:
    if response.status_code == 200:
        response_200 = Heartv2ListResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Heartv2ListResponse200]:
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
    startdate: Union[Unset, int] = UNSET,
    enddate: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[Heartv2ListResponse200]:
    """Heart v2  - List

     Returns a list of ECG records and Afib classification for a given period of time.
    To get the full ECG signal, use the [Heart v2 - Get](#operation/heartv2-get) service.

    If the ECG recordings have been taken with BPM Core, systole and diastole measurements will also be
    returned.

    Args:
        action (str):
        startdate (Union[Unset, int]):
        enddate (Union[Unset, int]):
        offset (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Heartv2ListResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        startdate=startdate,
        enddate=enddate,
        offset=offset,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    startdate: Union[Unset, int] = UNSET,
    enddate: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[Heartv2ListResponse200]:
    """Heart v2  - List

     Returns a list of ECG records and Afib classification for a given period of time.
    To get the full ECG signal, use the [Heart v2 - Get](#operation/heartv2-get) service.

    If the ECG recordings have been taken with BPM Core, systole and diastole measurements will also be
    returned.

    Args:
        action (str):
        startdate (Union[Unset, int]):
        enddate (Union[Unset, int]):
        offset (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Heartv2ListResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        startdate=startdate,
        enddate=enddate,
        offset=offset,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    startdate: Union[Unset, int] = UNSET,
    enddate: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[Heartv2ListResponse200]:
    """Heart v2  - List

     Returns a list of ECG records and Afib classification for a given period of time.
    To get the full ECG signal, use the [Heart v2 - Get](#operation/heartv2-get) service.

    If the ECG recordings have been taken with BPM Core, systole and diastole measurements will also be
    returned.

    Args:
        action (str):
        startdate (Union[Unset, int]):
        enddate (Union[Unset, int]):
        offset (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Heartv2ListResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        startdate=startdate,
        enddate=enddate,
        offset=offset,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    startdate: Union[Unset, int] = UNSET,
    enddate: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[Heartv2ListResponse200]:
    """Heart v2  - List

     Returns a list of ECG records and Afib classification for a given period of time.
    To get the full ECG signal, use the [Heart v2 - Get](#operation/heartv2-get) service.

    If the ECG recordings have been taken with BPM Core, systole and diastole measurements will also be
    returned.

    Args:
        action (str):
        startdate (Union[Unset, int]):
        enddate (Union[Unset, int]):
        offset (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Heartv2ListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            startdate=startdate,
            enddate=enddate,
            offset=offset,
            authorization=authorization,
        )
    ).parsed
