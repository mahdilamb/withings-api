from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dropshipmentv_2_update_response_200 import Dropshipmentv2UpdateResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: str,
    client_id: str,
    signature: str,
    nonce: str,
    order_id: str,
    order: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["client_id"] = client_id

    params["signature"] = signature

    params["nonce"] = nonce

    params["order_id"] = order_id

    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/dropshipment",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Dropshipmentv2UpdateResponse200]:
    if response.status_code == 200:
        response_200 = Dropshipmentv2UpdateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Dropshipmentv2UpdateResponse200]:
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
    order_id: str,
    order: str,
) -> Response[Dropshipmentv2UpdateResponse200]:
    """Dropshipment v2  - Update

     Updates a dropshipment order.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        order_id (str):
        order (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dropshipmentv2UpdateResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        order_id=order_id,
        order=order,
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
    order_id: str,
    order: str,
) -> Optional[Dropshipmentv2UpdateResponse200]:
    """Dropshipment v2  - Update

     Updates a dropshipment order.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        order_id (str):
        order (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dropshipmentv2UpdateResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        order_id=order_id,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    signature: str,
    nonce: str,
    order_id: str,
    order: str,
) -> Response[Dropshipmentv2UpdateResponse200]:
    """Dropshipment v2  - Update

     Updates a dropshipment order.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        order_id (str):
        order (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dropshipmentv2UpdateResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        order_id=order_id,
        order=order,
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
    order_id: str,
    order: str,
) -> Optional[Dropshipmentv2UpdateResponse200]:
    """Dropshipment v2  - Update

     Updates a dropshipment order.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        order_id (str):
        order (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dropshipmentv2UpdateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            client_id=client_id,
            signature=signature,
            nonce=nonce,
            order_id=order_id,
            order=order,
        )
    ).parsed
