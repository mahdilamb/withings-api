from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sleepv_2_get_response_200 import Sleepv2GetResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    startdate: int,
    enddate: int,
    data_fields: Union[Unset, str] = UNSET,
    meastypes: Union[Unset, str] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["startdate"] = startdate

    params["enddate"] = enddate

    params["data_fields"] = data_fields

    params["meastypes"] = meastypes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/sleep",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Sleepv2GetResponse200]:
    if response.status_code == 200:
        response_200 = Sleepv2GetResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Sleepv2GetResponse200]:
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
    startdate: int,
    enddate: int,
    data_fields: Union[Unset, str] = UNSET,
    meastypes: Union[Unset, str] = UNSET,
    authorization: str,
) -> Response[Sleepv2GetResponse200]:
    """Sleep v2  - Get

     Returns sleep data captured at high frequency, including sleep stages.

    **Notes:**

     - If your input ```startdate``` and ```enddate``` are separated by more than 24h, only the first
    24h after ```startdate``` will be returned.

    Args:
        action (str):
        startdate (int):
        enddate (int):
        data_fields (Union[Unset, str]):
        meastypes (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Sleepv2GetResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        startdate=startdate,
        enddate=enddate,
        data_fields=data_fields,
        meastypes=meastypes,
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
    startdate: int,
    enddate: int,
    data_fields: Union[Unset, str] = UNSET,
    meastypes: Union[Unset, str] = UNSET,
    authorization: str,
) -> Optional[Sleepv2GetResponse200]:
    """Sleep v2  - Get

     Returns sleep data captured at high frequency, including sleep stages.

    **Notes:**

     - If your input ```startdate``` and ```enddate``` are separated by more than 24h, only the first
    24h after ```startdate``` will be returned.

    Args:
        action (str):
        startdate (int):
        enddate (int):
        data_fields (Union[Unset, str]):
        meastypes (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Sleepv2GetResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        startdate=startdate,
        enddate=enddate,
        data_fields=data_fields,
        meastypes=meastypes,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    startdate: int,
    enddate: int,
    data_fields: Union[Unset, str] = UNSET,
    meastypes: Union[Unset, str] = UNSET,
    authorization: str,
) -> Response[Sleepv2GetResponse200]:
    """Sleep v2  - Get

     Returns sleep data captured at high frequency, including sleep stages.

    **Notes:**

     - If your input ```startdate``` and ```enddate``` are separated by more than 24h, only the first
    24h after ```startdate``` will be returned.

    Args:
        action (str):
        startdate (int):
        enddate (int):
        data_fields (Union[Unset, str]):
        meastypes (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Sleepv2GetResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        startdate=startdate,
        enddate=enddate,
        data_fields=data_fields,
        meastypes=meastypes,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    startdate: int,
    enddate: int,
    data_fields: Union[Unset, str] = UNSET,
    meastypes: Union[Unset, str] = UNSET,
    authorization: str,
) -> Optional[Sleepv2GetResponse200]:
    """Sleep v2  - Get

     Returns sleep data captured at high frequency, including sleep stages.

    **Notes:**

     - If your input ```startdate``` and ```enddate``` are separated by more than 24h, only the first
    24h after ```startdate``` will be returned.

    Args:
        action (str):
        startdate (int):
        enddate (int):
        data_fields (Union[Unset, str]):
        meastypes (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Sleepv2GetResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            startdate=startdate,
            enddate=enddate,
            data_fields=data_fields,
            meastypes=meastypes,
            authorization=authorization,
        )
    ).parsed
