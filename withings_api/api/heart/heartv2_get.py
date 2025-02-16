from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.heartv_2_get_response_200 import Heartv2GetResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    signalid: int,
    client_id: str,
    signature: str,
    nonce: str,
    signal_token: str,
    with_filtered: Union[Unset, bool] = UNSET,
    with_intervals: Union[Unset, bool] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["signalid"] = signalid

    params["client_id"] = client_id

    params["signature"] = signature

    params["nonce"] = nonce

    params["signal_token"] = signal_token

    params["with_filtered"] = with_filtered

    params["with_intervals"] = with_intervals

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/heart",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Heartv2GetResponse200]:
    if response.status_code == 200:
        response_200 = Heartv2GetResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Heartv2GetResponse200]:
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
    client_id: str,
    signature: str,
    nonce: str,
    signal_token: str,
    with_filtered: Union[Unset, bool] = UNSET,
    with_intervals: Union[Unset, bool] = UNSET,
    authorization: str,
) -> Response[Heartv2GetResponse200]:
    """Heart v2  - Get

     Provides the high frequency data of an ECG recording in micro-volt (μV).

    **Duration:**

     - BPM Core: 20 seconds.
     - Move ECG: 30 seconds.
     - ScanWatch: 30 seconds.

    **Sampling frequency:**

     - BPM Core: 500 Hz.
     - Move ECG: 300 Hz.
     - ScanWatch: 300 Hz.

    Args:
        action (str):
        signalid (int):
        client_id (str):
        signature (str):
        nonce (str):
        signal_token (str):
        with_filtered (Union[Unset, bool]):
        with_intervals (Union[Unset, bool]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Heartv2GetResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signalid=signalid,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        signal_token=signal_token,
        with_filtered=with_filtered,
        with_intervals=with_intervals,
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
    client_id: str,
    signature: str,
    nonce: str,
    signal_token: str,
    with_filtered: Union[Unset, bool] = UNSET,
    with_intervals: Union[Unset, bool] = UNSET,
    authorization: str,
) -> Optional[Heartv2GetResponse200]:
    """Heart v2  - Get

     Provides the high frequency data of an ECG recording in micro-volt (μV).

    **Duration:**

     - BPM Core: 20 seconds.
     - Move ECG: 30 seconds.
     - ScanWatch: 30 seconds.

    **Sampling frequency:**

     - BPM Core: 500 Hz.
     - Move ECG: 300 Hz.
     - ScanWatch: 300 Hz.

    Args:
        action (str):
        signalid (int):
        client_id (str):
        signature (str):
        nonce (str):
        signal_token (str):
        with_filtered (Union[Unset, bool]):
        with_intervals (Union[Unset, bool]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Heartv2GetResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        signalid=signalid,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        signal_token=signal_token,
        with_filtered=with_filtered,
        with_intervals=with_intervals,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signalid: int,
    client_id: str,
    signature: str,
    nonce: str,
    signal_token: str,
    with_filtered: Union[Unset, bool] = UNSET,
    with_intervals: Union[Unset, bool] = UNSET,
    authorization: str,
) -> Response[Heartv2GetResponse200]:
    """Heart v2  - Get

     Provides the high frequency data of an ECG recording in micro-volt (μV).

    **Duration:**

     - BPM Core: 20 seconds.
     - Move ECG: 30 seconds.
     - ScanWatch: 30 seconds.

    **Sampling frequency:**

     - BPM Core: 500 Hz.
     - Move ECG: 300 Hz.
     - ScanWatch: 300 Hz.

    Args:
        action (str):
        signalid (int):
        client_id (str):
        signature (str):
        nonce (str):
        signal_token (str):
        with_filtered (Union[Unset, bool]):
        with_intervals (Union[Unset, bool]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Heartv2GetResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signalid=signalid,
        client_id=client_id,
        signature=signature,
        nonce=nonce,
        signal_token=signal_token,
        with_filtered=with_filtered,
        with_intervals=with_intervals,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signalid: int,
    client_id: str,
    signature: str,
    nonce: str,
    signal_token: str,
    with_filtered: Union[Unset, bool] = UNSET,
    with_intervals: Union[Unset, bool] = UNSET,
    authorization: str,
) -> Optional[Heartv2GetResponse200]:
    """Heart v2  - Get

     Provides the high frequency data of an ECG recording in micro-volt (μV).

    **Duration:**

     - BPM Core: 20 seconds.
     - Move ECG: 30 seconds.
     - ScanWatch: 30 seconds.

    **Sampling frequency:**

     - BPM Core: 500 Hz.
     - Move ECG: 300 Hz.
     - ScanWatch: 300 Hz.

    Args:
        action (str):
        signalid (int):
        client_id (str):
        signature (str):
        nonce (str):
        signal_token (str):
        with_filtered (Union[Unset, bool]):
        with_intervals (Union[Unset, bool]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Heartv2GetResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            signalid=signalid,
            client_id=client_id,
            signature=signature,
            nonce=nonce,
            signal_token=signal_token,
            with_filtered=with_filtered,
            with_intervals=with_intervals,
            authorization=authorization,
        )
    ).parsed
