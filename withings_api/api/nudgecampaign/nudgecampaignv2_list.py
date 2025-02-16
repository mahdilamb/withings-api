from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nudgecampaignv_2_list_response_200 import Nudgecampaignv2ListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    offset: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["signature"] = signature

    params["client_id"] = client_id

    params["nonce"] = nonce

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/nudgecampaign",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Nudgecampaignv2ListResponse200]:
    if response.status_code == 200:
        response_200 = Nudgecampaignv2ListResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Nudgecampaignv2ListResponse200]:
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
    offset: Union[Unset, int] = UNSET,
) -> Response[Nudgecampaignv2ListResponse200]:
    """Nudgecampaign v2  - List

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Nudgecampaignv2ListResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        offset=offset,
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
    offset: Union[Unset, int] = UNSET,
) -> Optional[Nudgecampaignv2ListResponse200]:
    """Nudgecampaign v2  - List

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Nudgecampaignv2ListResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    offset: Union[Unset, int] = UNSET,
) -> Response[Nudgecampaignv2ListResponse200]:
    """Nudgecampaign v2  - List

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Nudgecampaignv2ListResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        offset=offset,
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
    offset: Union[Unset, int] = UNSET,
) -> Optional[Nudgecampaignv2ListResponse200]:
    """Nudgecampaign v2  - List

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Nudgecampaignv2ListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            signature=signature,
            client_id=client_id,
            nonce=nonce,
            offset=offset,
        )
    ).parsed
