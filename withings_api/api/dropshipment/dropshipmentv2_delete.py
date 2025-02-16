from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dropshipmentv_2_delete_response_200 import Dropshipmentv2DeleteResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: str,
    client_id: str,
    signature: str,
    nonce: str,
    order_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["client_id"] = client_id

    params["signature"] = signature

    params["nonce"] = nonce

    params["order_id"] = order_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/dropshipment",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Dropshipmentv2DeleteResponse200]:
    if response.status_code == 200:
        response_200 = Dropshipmentv2DeleteResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Dropshipmentv2DeleteResponse200]:
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
) -> Response[Dropshipmentv2DeleteResponse200]:
    """Dropshipment v2  - Delete

     Cancels a dropshipment order.
    Only orders that haven't been shipped can be cancelled.
    Note that there can be a latency between the shipping of the parcel and the update of the shipping
    status to *SHIPPED*.
    Trying to cancel an order that was already shipped will result in a error with error code 277.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dropshipmentv2DeleteResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        order_id=order_id,
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
) -> Optional[Dropshipmentv2DeleteResponse200]:
    """Dropshipment v2  - Delete

     Cancels a dropshipment order.
    Only orders that haven't been shipped can be cancelled.
    Note that there can be a latency between the shipping of the parcel and the update of the shipping
    status to *SHIPPED*.
    Trying to cancel an order that was already shipped will result in a error with error code 277.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dropshipmentv2DeleteResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        order_id=order_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    signature: str,
    nonce: str,
    order_id: str,
) -> Response[Dropshipmentv2DeleteResponse200]:
    """Dropshipment v2  - Delete

     Cancels a dropshipment order.
    Only orders that haven't been shipped can be cancelled.
    Note that there can be a latency between the shipping of the parcel and the update of the shipping
    status to *SHIPPED*.
    Trying to cancel an order that was already shipped will result in a error with error code 277.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dropshipmentv2DeleteResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        order_id=order_id,
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
) -> Optional[Dropshipmentv2DeleteResponse200]:
    """Dropshipment v2  - Delete

     Cancels a dropshipment order.
    Only orders that haven't been shipped can be cancelled.
    Note that there can be a latency between the shipping of the parcel and the update of the shipping
    status to *SHIPPED*.
    Trying to cancel an order that was already shipped will result in a error with error code 277.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dropshipmentv2DeleteResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            client_id=client_id,
            signature=signature,
            nonce=nonce,
            order_id=order_id,
        )
    ).parsed
