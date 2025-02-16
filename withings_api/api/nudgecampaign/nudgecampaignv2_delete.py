from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nudgecampaignv_2_delete_response_200 import Nudgecampaignv2DeleteResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    nudgecampaignid: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["signature"] = signature

    params["client_id"] = client_id

    params["nonce"] = nonce

    params["nudgecampaignid"] = nudgecampaignid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/nudgecampaign",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Nudgecampaignv2DeleteResponse200]:
    if response.status_code == 200:
        response_200 = Nudgecampaignv2DeleteResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Nudgecampaignv2DeleteResponse200]:
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
    nudgecampaignid: int,
) -> Response[Nudgecampaignv2DeleteResponse200]:
    """Nudgecampaign v2  - Delete

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        nudgecampaignid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Nudgecampaignv2DeleteResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        nudgecampaignid=nudgecampaignid,
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
    nudgecampaignid: int,
) -> Optional[Nudgecampaignv2DeleteResponse200]:
    """Nudgecampaign v2  - Delete

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        nudgecampaignid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Nudgecampaignv2DeleteResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        nudgecampaignid=nudgecampaignid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    nudgecampaignid: int,
) -> Response[Nudgecampaignv2DeleteResponse200]:
    """Nudgecampaign v2  - Delete

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        nudgecampaignid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Nudgecampaignv2DeleteResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        nudgecampaignid=nudgecampaignid,
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
    nudgecampaignid: int,
) -> Optional[Nudgecampaignv2DeleteResponse200]:
    """Nudgecampaign v2  - Delete

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        nudgecampaignid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Nudgecampaignv2DeleteResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            signature=signature,
            client_id=client_id,
            nonce=nonce,
            nudgecampaignid=nudgecampaignid,
        )
    ).parsed
