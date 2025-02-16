from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nudgev_2_update_response_200 import Nudgev2UpdateResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    nudgeid: int,
    iconids: Union[Unset, str] = UNSET,
    content: Union[Unset, str] = UNSET,
    model: Union[Unset, int] = UNSET,
    position: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["signature"] = signature

    params["client_id"] = client_id

    params["nonce"] = nonce

    params["nudgeid"] = nudgeid

    params["iconids"] = iconids

    params["content"] = content

    params["model"] = model

    params["position"] = position

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/nudge",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Nudgev2UpdateResponse200]:
    if response.status_code == 200:
        response_200 = Nudgev2UpdateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Nudgev2UpdateResponse200]:
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
    nudgeid: int,
    iconids: Union[Unset, str] = UNSET,
    content: Union[Unset, str] = UNSET,
    model: Union[Unset, int] = UNSET,
    position: Union[Unset, str] = UNSET,
) -> Response[Nudgev2UpdateResponse200]:
    """Nudge v2  - Update

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        nudgeid (int):
        iconids (Union[Unset, str]):
        content (Union[Unset, str]):
        model (Union[Unset, int]):
        position (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Nudgev2UpdateResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        nudgeid=nudgeid,
        iconids=iconids,
        content=content,
        model=model,
        position=position,
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
    nudgeid: int,
    iconids: Union[Unset, str] = UNSET,
    content: Union[Unset, str] = UNSET,
    model: Union[Unset, int] = UNSET,
    position: Union[Unset, str] = UNSET,
) -> Optional[Nudgev2UpdateResponse200]:
    """Nudge v2  - Update

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        nudgeid (int):
        iconids (Union[Unset, str]):
        content (Union[Unset, str]):
        model (Union[Unset, int]):
        position (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Nudgev2UpdateResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        nudgeid=nudgeid,
        iconids=iconids,
        content=content,
        model=model,
        position=position,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    nudgeid: int,
    iconids: Union[Unset, str] = UNSET,
    content: Union[Unset, str] = UNSET,
    model: Union[Unset, int] = UNSET,
    position: Union[Unset, str] = UNSET,
) -> Response[Nudgev2UpdateResponse200]:
    """Nudge v2  - Update

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        nudgeid (int):
        iconids (Union[Unset, str]):
        content (Union[Unset, str]):
        model (Union[Unset, int]):
        position (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Nudgev2UpdateResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        nudgeid=nudgeid,
        iconids=iconids,
        content=content,
        model=model,
        position=position,
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
    nudgeid: int,
    iconids: Union[Unset, str] = UNSET,
    content: Union[Unset, str] = UNSET,
    model: Union[Unset, int] = UNSET,
    position: Union[Unset, str] = UNSET,
) -> Optional[Nudgev2UpdateResponse200]:
    """Nudge v2  - Update

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        nudgeid (int):
        iconids (Union[Unset, str]):
        content (Union[Unset, str]):
        model (Union[Unset, int]):
        position (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Nudgev2UpdateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            signature=signature,
            client_id=client_id,
            nonce=nonce,
            nudgeid=nudgeid,
            iconids=iconids,
            content=content,
            model=model,
            position=position,
        )
    ).parsed
