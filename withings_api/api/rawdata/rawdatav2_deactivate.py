from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rawdatav_2_deactivate_response_200 import Rawdatav2DeactivateResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    hash_deviceid: str,
    rawdata_type: Union[Unset, int] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["hash_deviceid"] = hash_deviceid

    params["rawdata_type"] = rawdata_type

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
) -> Optional[Rawdatav2DeactivateResponse200]:
    if response.status_code == 200:
        response_200 = Rawdatav2DeactivateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Rawdatav2DeactivateResponse200]:
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
    rawdata_type: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[Rawdatav2DeactivateResponse200]:
    """Rawdata v2  - Deactivate

     This service allows the de-activation of raw data collection. Raw Data de-activation will occur as
    soon as the Withings device is able to sync with the Withings app.

    Args:
        action (str):
        hash_deviceid (str):
        rawdata_type (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Rawdatav2DeactivateResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        hash_deviceid=hash_deviceid,
        rawdata_type=rawdata_type,
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
    rawdata_type: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[Rawdatav2DeactivateResponse200]:
    """Rawdata v2  - Deactivate

     This service allows the de-activation of raw data collection. Raw Data de-activation will occur as
    soon as the Withings device is able to sync with the Withings app.

    Args:
        action (str):
        hash_deviceid (str):
        rawdata_type (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Rawdatav2DeactivateResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        hash_deviceid=hash_deviceid,
        rawdata_type=rawdata_type,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    hash_deviceid: str,
    rawdata_type: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[Rawdatav2DeactivateResponse200]:
    """Rawdata v2  - Deactivate

     This service allows the de-activation of raw data collection. Raw Data de-activation will occur as
    soon as the Withings device is able to sync with the Withings app.

    Args:
        action (str):
        hash_deviceid (str):
        rawdata_type (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Rawdatav2DeactivateResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        hash_deviceid=hash_deviceid,
        rawdata_type=rawdata_type,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    hash_deviceid: str,
    rawdata_type: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[Rawdatav2DeactivateResponse200]:
    """Rawdata v2  - Deactivate

     This service allows the de-activation of raw data collection. Raw Data de-activation will occur as
    soon as the Withings device is able to sync with the Withings app.

    Args:
        action (str):
        hash_deviceid (str):
        rawdata_type (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Rawdatav2DeactivateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            hash_deviceid=hash_deviceid,
            rawdata_type=rawdata_type,
            authorization=authorization,
        )
    ).parsed
