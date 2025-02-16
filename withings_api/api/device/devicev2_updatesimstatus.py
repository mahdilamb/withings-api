from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.devicev_2_updatesimstatus_response_200 import Devicev2UpdatesimstatusResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: str,
    client_id: str,
    signature: str,
    nonce: str,
    mac_address: str,
    sim_status: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["client_id"] = client_id

    params["signature"] = signature

    params["nonce"] = nonce

    params["mac_address"] = mac_address

    params["sim_status"] = sim_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/device",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Devicev2UpdatesimstatusResponse200]:
    if response.status_code == 200:
        response_200 = Devicev2UpdatesimstatusResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Devicev2UpdatesimstatusResponse200]:
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
    signature: str,
    nonce: str,
    mac_address: str,
    sim_status: str,
) -> Response[Devicev2UpdatesimstatusResponse200]:
    """Device v2  - Updatesimstatus

     **Important:** Read the [Terminate Device](/developer-guide/v3/integration-guide/terminatecellular)
    Section before calling this webservice.

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        mac_address (str):
        sim_status (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Devicev2UpdatesimstatusResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        mac_address=mac_address,
        sim_status=sim_status,
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
    signature: str,
    nonce: str,
    mac_address: str,
    sim_status: str,
) -> Optional[Devicev2UpdatesimstatusResponse200]:
    """Device v2  - Updatesimstatus

     **Important:** Read the [Terminate Device](/developer-guide/v3/integration-guide/terminatecellular)
    Section before calling this webservice.

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        mac_address (str):
        sim_status (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Devicev2UpdatesimstatusResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        mac_address=mac_address,
        sim_status=sim_status,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    signature: str,
    nonce: str,
    mac_address: str,
    sim_status: str,
) -> Response[Devicev2UpdatesimstatusResponse200]:
    """Device v2  - Updatesimstatus

     **Important:** Read the [Terminate Device](/developer-guide/v3/integration-guide/terminatecellular)
    Section before calling this webservice.

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        mac_address (str):
        sim_status (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Devicev2UpdatesimstatusResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        mac_address=mac_address,
        sim_status=sim_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    signature: str,
    nonce: str,
    mac_address: str,
    sim_status: str,
) -> Optional[Devicev2UpdatesimstatusResponse200]:
    """Device v2  - Updatesimstatus

     **Important:** Read the [Terminate Device](/developer-guide/v3/integration-guide/terminatecellular)
    Section before calling this webservice.

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        mac_address (str):
        sim_status (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Devicev2UpdatesimstatusResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            client_id=client_id,
            signature=signature,
            nonce=nonce,
            mac_address=mac_address,
            sim_status=sim_status,
        )
    ).parsed
