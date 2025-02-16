from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rawdatav_2_get_response_200 import Rawdatav2GetResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    hash_deviceid: str,
    rawdata_type: int,
    startdate: int,
    enddate: int,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["hash_deviceid"] = hash_deviceid

    params["rawdata_type"] = rawdata_type

    params["startdate"] = startdate

    params["enddate"] = enddate

    params["offset"] = offset

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
) -> Optional[Rawdatav2GetResponse200]:
    if response.status_code == 200:
        response_200 = Rawdatav2GetResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Rawdatav2GetResponse200]:
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
    startdate: int,
    enddate: int,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[Rawdatav2GetResponse200]:
    """Rawdata v2  - Get

     This service allows to fetch raw data of a specific type that were captured and synchronized by a
    Withings device. Detailled information about the data structure can be found in the [Raw Data
    structure section](/developer-guide/v3/integration-guide/advanced-research-api/fetch-raw-data/raw-
    data-structure).

    Args:
        action (str):
        hash_deviceid (str):
        rawdata_type (int):
        startdate (int):
        enddate (int):
        offset (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Rawdatav2GetResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        hash_deviceid=hash_deviceid,
        rawdata_type=rawdata_type,
        startdate=startdate,
        enddate=enddate,
        offset=offset,
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
    startdate: int,
    enddate: int,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[Rawdatav2GetResponse200]:
    """Rawdata v2  - Get

     This service allows to fetch raw data of a specific type that were captured and synchronized by a
    Withings device. Detailled information about the data structure can be found in the [Raw Data
    structure section](/developer-guide/v3/integration-guide/advanced-research-api/fetch-raw-data/raw-
    data-structure).

    Args:
        action (str):
        hash_deviceid (str):
        rawdata_type (int):
        startdate (int):
        enddate (int):
        offset (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Rawdatav2GetResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        hash_deviceid=hash_deviceid,
        rawdata_type=rawdata_type,
        startdate=startdate,
        enddate=enddate,
        offset=offset,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    hash_deviceid: str,
    rawdata_type: int,
    startdate: int,
    enddate: int,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[Rawdatav2GetResponse200]:
    """Rawdata v2  - Get

     This service allows to fetch raw data of a specific type that were captured and synchronized by a
    Withings device. Detailled information about the data structure can be found in the [Raw Data
    structure section](/developer-guide/v3/integration-guide/advanced-research-api/fetch-raw-data/raw-
    data-structure).

    Args:
        action (str):
        hash_deviceid (str):
        rawdata_type (int):
        startdate (int):
        enddate (int):
        offset (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Rawdatav2GetResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        hash_deviceid=hash_deviceid,
        rawdata_type=rawdata_type,
        startdate=startdate,
        enddate=enddate,
        offset=offset,
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
    startdate: int,
    enddate: int,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[Rawdatav2GetResponse200]:
    """Rawdata v2  - Get

     This service allows to fetch raw data of a specific type that were captured and synchronized by a
    Withings device. Detailled information about the data structure can be found in the [Raw Data
    structure section](/developer-guide/v3/integration-guide/advanced-research-api/fetch-raw-data/raw-
    data-structure).

    Args:
        action (str):
        hash_deviceid (str):
        rawdata_type (int):
        startdate (int):
        enddate (int):
        offset (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Rawdatav2GetResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            hash_deviceid=hash_deviceid,
            rawdata_type=rawdata_type,
            startdate=startdate,
            enddate=enddate,
            offset=offset,
            authorization=authorization,
        )
    ).parsed
