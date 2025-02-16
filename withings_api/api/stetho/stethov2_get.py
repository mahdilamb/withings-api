from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stethov_2_get_response_200 import Stethov2GetResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: str,
    signalid: int,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["signalid"] = signalid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/stetho",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Stethov2GetResponse200]:
    if response.status_code == 200:
        response_200 = Stethov2GetResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Stethov2GetResponse200]:
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
    signalid: int,
    authorization: str,
) -> Response[Stethov2GetResponse200]:
    """Stetho v2  - Get

    Args:
        action (str):
        signalid (int):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Stethov2GetResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signalid=signalid,
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
    signalid: int,
    authorization: str,
) -> Optional[Stethov2GetResponse200]:
    """Stetho v2  - Get

    Args:
        action (str):
        signalid (int):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Stethov2GetResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        signalid=signalid,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signalid: int,
    authorization: str,
) -> Response[Stethov2GetResponse200]:
    """Stetho v2  - Get

    Args:
        action (str):
        signalid (int):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Stethov2GetResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signalid=signalid,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signalid: int,
    authorization: str,
) -> Optional[Stethov2GetResponse200]:
    """Stetho v2  - Get

    Args:
        action (str):
        signalid (int):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Stethov2GetResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            signalid=signalid,
            authorization=authorization,
        )
    ).parsed
