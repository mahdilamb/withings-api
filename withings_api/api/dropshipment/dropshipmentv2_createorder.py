from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dropshipmentv_2_createorder_response_200 import Dropshipmentv2CreateorderResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    client_id: str,
    nonce: str,
    signature: str,
    order: str,
    customerid: Union[Unset, str] = UNSET,
    testmode: Union[Unset, int] = UNSET,
    platformid: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["client_id"] = client_id

    params["nonce"] = nonce

    params["signature"] = signature

    params["order"] = order

    params["customerid"] = customerid

    params["testmode"] = testmode

    params["platformid"] = platformid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/dropshipment",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Dropshipmentv2CreateorderResponse200]:
    if response.status_code == 200:
        response_200 = Dropshipmentv2CreateorderResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Dropshipmentv2CreateorderResponse200]:
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
    order: str,
    customerid: Union[Unset, str] = UNSET,
    testmode: Union[Unset, int] = UNSET,
    platformid: Union[Unset, int] = UNSET,
) -> Response[Dropshipmentv2CreateorderResponse200]:
    """Dropshipment v2  - Createorder

     Creates a dropshipment order.

    If one of the orders has an invalid address, none of the orders will be created.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*
    *Do not use this service if you're integrating Withings Cellular Solutions with dropshipment. In
    that case, please use the createuserorder action*

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        order (str):
        customerid (Union[Unset, str]):
        testmode (Union[Unset, int]):
        platformid (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dropshipmentv2CreateorderResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        nonce=nonce,
        signature=signature,
        order=order,
        customerid=customerid,
        testmode=testmode,
        platformid=platformid,
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
    order: str,
    customerid: Union[Unset, str] = UNSET,
    testmode: Union[Unset, int] = UNSET,
    platformid: Union[Unset, int] = UNSET,
) -> Optional[Dropshipmentv2CreateorderResponse200]:
    """Dropshipment v2  - Createorder

     Creates a dropshipment order.

    If one of the orders has an invalid address, none of the orders will be created.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*
    *Do not use this service if you're integrating Withings Cellular Solutions with dropshipment. In
    that case, please use the createuserorder action*

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        order (str):
        customerid (Union[Unset, str]):
        testmode (Union[Unset, int]):
        platformid (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dropshipmentv2CreateorderResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        client_id=client_id,
        nonce=nonce,
        signature=signature,
        order=order,
        customerid=customerid,
        testmode=testmode,
        platformid=platformid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    nonce: str,
    signature: str,
    order: str,
    customerid: Union[Unset, str] = UNSET,
    testmode: Union[Unset, int] = UNSET,
    platformid: Union[Unset, int] = UNSET,
) -> Response[Dropshipmentv2CreateorderResponse200]:
    """Dropshipment v2  - Createorder

     Creates a dropshipment order.

    If one of the orders has an invalid address, none of the orders will be created.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*
    *Do not use this service if you're integrating Withings Cellular Solutions with dropshipment. In
    that case, please use the createuserorder action*

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        order (str):
        customerid (Union[Unset, str]):
        testmode (Union[Unset, int]):
        platformid (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dropshipmentv2CreateorderResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        nonce=nonce,
        signature=signature,
        order=order,
        customerid=customerid,
        testmode=testmode,
        platformid=platformid,
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
    order: str,
    customerid: Union[Unset, str] = UNSET,
    testmode: Union[Unset, int] = UNSET,
    platformid: Union[Unset, int] = UNSET,
) -> Optional[Dropshipmentv2CreateorderResponse200]:
    """Dropshipment v2  - Createorder

     Creates a dropshipment order.

    If one of the orders has an invalid address, none of the orders will be created.

    *This service is part of Withings Pro Solutions. You won't be able to use it if you did not sign a
    contract with Withings.*
    *Do not use this service if you're integrating Withings Cellular Solutions with dropshipment. In
    that case, please use the createuserorder action*

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        order (str):
        customerid (Union[Unset, str]):
        testmode (Union[Unset, int]):
        platformid (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dropshipmentv2CreateorderResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            client_id=client_id,
            nonce=nonce,
            signature=signature,
            order=order,
            customerid=customerid,
            testmode=testmode,
            platformid=platformid,
        )
    ).parsed
