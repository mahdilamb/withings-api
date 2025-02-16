from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.devicev_2_disablefeature_response_200 import Devicev2DisablefeatureResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: str,
    client_id: str,
    signature: str,
    nonce: str,
    feature_name: str,
    userid: int,
    model: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["client_id"] = client_id

    params["signature"] = signature

    params["nonce"] = nonce

    params["feature_name"] = feature_name

    params["userid"] = userid

    params["model"] = model

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/device",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Devicev2DisablefeatureResponse200]:
    if response.status_code == 200:
        response_200 = Devicev2DisablefeatureResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Devicev2DisablefeatureResponse200]:
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
    feature_name: str,
    userid: int,
    model: int,
) -> Response[Devicev2DisablefeatureResponse200]:
    """Device v2  - Disablefeature

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        feature_name (str):
        userid (int):
        model (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Devicev2DisablefeatureResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        feature_name=feature_name,
        userid=userid,
        model=model,
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
    feature_name: str,
    userid: int,
    model: int,
) -> Optional[Devicev2DisablefeatureResponse200]:
    """Device v2  - Disablefeature

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        feature_name (str):
        userid (int):
        model (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Devicev2DisablefeatureResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        feature_name=feature_name,
        userid=userid,
        model=model,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    signature: str,
    nonce: str,
    feature_name: str,
    userid: int,
    model: int,
) -> Response[Devicev2DisablefeatureResponse200]:
    """Device v2  - Disablefeature

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        feature_name (str):
        userid (int):
        model (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Devicev2DisablefeatureResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        feature_name=feature_name,
        userid=userid,
        model=model,
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
    feature_name: str,
    userid: int,
    model: int,
) -> Optional[Devicev2DisablefeatureResponse200]:
    """Device v2  - Disablefeature

    Args:
        action (str):
        client_id (str):
        signature (str):
        nonce (str):
        feature_name (str):
        userid (int):
        model (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Devicev2DisablefeatureResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            client_id=client_id,
            signature=signature,
            nonce=nonce,
            feature_name=feature_name,
            userid=userid,
            model=model,
        )
    ).parsed
