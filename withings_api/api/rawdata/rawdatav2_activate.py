from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rawdatav_2_activate_response_200 import Rawdatav2ActivateResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    hash_deviceid: str,
    rawdata_type: int,
    enddate: Union[Unset, int] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["hash_deviceid"] = hash_deviceid

    params["rawdata_type"] = rawdata_type

    params["enddate"] = enddate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/rawdata",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Rawdatav2ActivateResponse200]:
    if response.status_code == 200:
        response_200 = Rawdatav2ActivateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Rawdatav2ActivateResponse200]:
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
    hash_deviceid: str,
    rawdata_type: int,
    enddate: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[Rawdatav2ActivateResponse200]:
    """Rawdata v2  - Activate

     This service allows to activate Raw Data collection on a given device that is already set up, and
    set the date at which the raw data collection will stop (enddate). The raw data capture will be
    activated as soon as the watch is able to sync with the Withings app following the API call. The
    capture will stop automatically at the enddate provided in the API call.

    Args:
        action (str):
        hash_deviceid (str):
        rawdata_type (int):
        enddate (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Rawdatav2ActivateResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        hash_deviceid=hash_deviceid,
        rawdata_type=rawdata_type,
        enddate=enddate,
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
    hash_deviceid: str,
    rawdata_type: int,
    enddate: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[Rawdatav2ActivateResponse200]:
    """Rawdata v2  - Activate

     This service allows to activate Raw Data collection on a given device that is already set up, and
    set the date at which the raw data collection will stop (enddate). The raw data capture will be
    activated as soon as the watch is able to sync with the Withings app following the API call. The
    capture will stop automatically at the enddate provided in the API call.

    Args:
        action (str):
        hash_deviceid (str):
        rawdata_type (int):
        enddate (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Rawdatav2ActivateResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        hash_deviceid=hash_deviceid,
        rawdata_type=rawdata_type,
        enddate=enddate,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    hash_deviceid: str,
    rawdata_type: int,
    enddate: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[Rawdatav2ActivateResponse200]:
    """Rawdata v2  - Activate

     This service allows to activate Raw Data collection on a given device that is already set up, and
    set the date at which the raw data collection will stop (enddate). The raw data capture will be
    activated as soon as the watch is able to sync with the Withings app following the API call. The
    capture will stop automatically at the enddate provided in the API call.

    Args:
        action (str):
        hash_deviceid (str):
        rawdata_type (int):
        enddate (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Rawdatav2ActivateResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        hash_deviceid=hash_deviceid,
        rawdata_type=rawdata_type,
        enddate=enddate,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    hash_deviceid: str,
    rawdata_type: int,
    enddate: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[Rawdatav2ActivateResponse200]:
    """Rawdata v2  - Activate

     This service allows to activate Raw Data collection on a given device that is already set up, and
    set the date at which the raw data collection will stop (enddate). The raw data capture will be
    activated as soon as the watch is able to sync with the Withings app following the API call. The
    capture will stop automatically at the enddate provided in the API call.

    Args:
        action (str):
        hash_deviceid (str):
        rawdata_type (int):
        enddate (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Rawdatav2ActivateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            hash_deviceid=hash_deviceid,
            rawdata_type=rawdata_type,
            enddate=enddate,
            authorization=authorization,
        )
    ).parsed
