from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.measurev_2_getintradayactivity_response_200 import Measurev2GetintradayactivityResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    startdate: Union[Unset, int] = UNSET,
    enddate: Union[Unset, int] = UNSET,
    data_fields: Union[Unset, str] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["startdate"] = startdate

    params["enddate"] = enddate

    params["data_fields"] = data_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/measure",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Measurev2GetintradayactivityResponse200]:
    if response.status_code == 200:
        response_200 = Measurev2GetintradayactivityResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Measurev2GetintradayactivityResponse200]:
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
    data_fields: Union[Unset, str] = UNSET,
    authorization: str,
) -> Response[Measurev2GetintradayactivityResponse200]:
    """Measure v2  - Getintradayactivity

     Returns user activity data captured at high frequency.

    **Notes:**

     - If your input ```startdate``` and ```enddate``` are separated by more than 24h, only the first
    24h after ```startdate``` will be returned.
     - If no ```startdate``` and ```enddate``` are passed as parameters, the most recent activity data
    will be returned.

    Args:
        action (str):
        startdate (Union[Unset, int]):
        enddate (Union[Unset, int]):
        data_fields (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Measurev2GetintradayactivityResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        startdate=startdate,
        enddate=enddate,
        data_fields=data_fields,
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
    data_fields: Union[Unset, str] = UNSET,
    authorization: str,
) -> Optional[Measurev2GetintradayactivityResponse200]:
    """Measure v2  - Getintradayactivity

     Returns user activity data captured at high frequency.

    **Notes:**

     - If your input ```startdate``` and ```enddate``` are separated by more than 24h, only the first
    24h after ```startdate``` will be returned.
     - If no ```startdate``` and ```enddate``` are passed as parameters, the most recent activity data
    will be returned.

    Args:
        action (str):
        startdate (Union[Unset, int]):
        enddate (Union[Unset, int]):
        data_fields (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Measurev2GetintradayactivityResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        startdate=startdate,
        enddate=enddate,
        data_fields=data_fields,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    startdate: Union[Unset, int] = UNSET,
    enddate: Union[Unset, int] = UNSET,
    data_fields: Union[Unset, str] = UNSET,
    authorization: str,
) -> Response[Measurev2GetintradayactivityResponse200]:
    """Measure v2  - Getintradayactivity

     Returns user activity data captured at high frequency.

    **Notes:**

     - If your input ```startdate``` and ```enddate``` are separated by more than 24h, only the first
    24h after ```startdate``` will be returned.
     - If no ```startdate``` and ```enddate``` are passed as parameters, the most recent activity data
    will be returned.

    Args:
        action (str):
        startdate (Union[Unset, int]):
        enddate (Union[Unset, int]):
        data_fields (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Measurev2GetintradayactivityResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        startdate=startdate,
        enddate=enddate,
        data_fields=data_fields,
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
    data_fields: Union[Unset, str] = UNSET,
    authorization: str,
) -> Optional[Measurev2GetintradayactivityResponse200]:
    """Measure v2  - Getintradayactivity

     Returns user activity data captured at high frequency.

    **Notes:**

     - If your input ```startdate``` and ```enddate``` are separated by more than 24h, only the first
    24h after ```startdate``` will be returned.
     - If no ```startdate``` and ```enddate``` are passed as parameters, the most recent activity data
    will be returned.

    Args:
        action (str):
        startdate (Union[Unset, int]):
        enddate (Union[Unset, int]):
        data_fields (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Measurev2GetintradayactivityResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            startdate=startdate,
            enddate=enddate,
            data_fields=data_fields,
            authorization=authorization,
        )
    ).parsed
