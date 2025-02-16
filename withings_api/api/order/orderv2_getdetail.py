from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.orderv_2_getdetail_response_200 import Orderv2GetdetailResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    client_id: str,
    nonce: str,
    signature: str,
    order_ids: str,
    customer_ref_ids: str,
    customerid: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["client_id"] = client_id

    params["nonce"] = nonce

    params["signature"] = signature

    params["order_ids"] = order_ids

    params["customer_ref_ids"] = customer_ref_ids

    params["customerid"] = customerid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/order",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Orderv2GetdetailResponse200]:
    if response.status_code == 200:
        response_200 = Orderv2GetdetailResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Orderv2GetdetailResponse200]:
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
    nonce: str,
    signature: str,
    order_ids: str,
    customer_ref_ids: str,
    customerid: Union[Unset, str] = UNSET,
) -> Response[Orderv2GetdetailResponse200]:
    """Order v2  - Getdetail

     Returns detailed information about bulkshipment or dropshipment orders.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        order_ids (str):
        customer_ref_ids (str):
        customerid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Orderv2GetdetailResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        nonce=nonce,
        signature=signature,
        order_ids=order_ids,
        customer_ref_ids=customer_ref_ids,
        customerid=customerid,
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
    nonce: str,
    signature: str,
    order_ids: str,
    customer_ref_ids: str,
    customerid: Union[Unset, str] = UNSET,
) -> Optional[Orderv2GetdetailResponse200]:
    """Order v2  - Getdetail

     Returns detailed information about bulkshipment or dropshipment orders.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        order_ids (str):
        customer_ref_ids (str):
        customerid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Orderv2GetdetailResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        client_id=client_id,
        nonce=nonce,
        signature=signature,
        order_ids=order_ids,
        customer_ref_ids=customer_ref_ids,
        customerid=customerid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    nonce: str,
    signature: str,
    order_ids: str,
    customer_ref_ids: str,
    customerid: Union[Unset, str] = UNSET,
) -> Response[Orderv2GetdetailResponse200]:
    """Order v2  - Getdetail

     Returns detailed information about bulkshipment or dropshipment orders.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        order_ids (str):
        customer_ref_ids (str):
        customerid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Orderv2GetdetailResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        nonce=nonce,
        signature=signature,
        order_ids=order_ids,
        customer_ref_ids=customer_ref_ids,
        customerid=customerid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    nonce: str,
    signature: str,
    order_ids: str,
    customer_ref_ids: str,
    customerid: Union[Unset, str] = UNSET,
) -> Optional[Orderv2GetdetailResponse200]:
    """Order v2  - Getdetail

     Returns detailed information about bulkshipment or dropshipment orders.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        order_ids (str):
        customer_ref_ids (str):
        customerid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Orderv2GetdetailResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            client_id=client_id,
            nonce=nonce,
            signature=signature,
            order_ids=order_ids,
            customer_ref_ids=customer_ref_ids,
            customerid=customerid,
        )
    ).parsed
