from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.measure_getmeas_response_200 import MeasureGetmeasResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    meastype: Union[Unset, int] = UNSET,
    meastypes: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
    startdate: Union[Unset, int] = UNSET,
    enddate: Union[Unset, int] = UNSET,
    lastupdate: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["meastype"] = meastype

    params["meastypes"] = meastypes

    params["category"] = category

    params["startdate"] = startdate

    params["enddate"] = enddate

    params["lastupdate"] = lastupdate

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/measure",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MeasureGetmeasResponse200]:
    if response.status_code == 200:
        response_200 = MeasureGetmeasResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MeasureGetmeasResponse200]:
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
    meastype: Union[Unset, int] = UNSET,
    meastypes: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
    startdate: Union[Unset, int] = UNSET,
    enddate: Union[Unset, int] = UNSET,
    lastupdate: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[MeasureGetmeasResponse200]:
    """Measure  - Getmeas

     Provides measures stored at a specific date among the types below. Please refer to the following
    responses for details.

    Args:
        action (str):
        meastype (Union[Unset, int]):
        meastypes (Union[Unset, str]):
        category (Union[Unset, int]):
        startdate (Union[Unset, int]):
        enddate (Union[Unset, int]):
        lastupdate (Union[Unset, int]):
        offset (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MeasureGetmeasResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        meastype=meastype,
        meastypes=meastypes,
        category=category,
        startdate=startdate,
        enddate=enddate,
        lastupdate=lastupdate,
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
    meastype: Union[Unset, int] = UNSET,
    meastypes: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
    startdate: Union[Unset, int] = UNSET,
    enddate: Union[Unset, int] = UNSET,
    lastupdate: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[MeasureGetmeasResponse200]:
    """Measure  - Getmeas

     Provides measures stored at a specific date among the types below. Please refer to the following
    responses for details.

    Args:
        action (str):
        meastype (Union[Unset, int]):
        meastypes (Union[Unset, str]):
        category (Union[Unset, int]):
        startdate (Union[Unset, int]):
        enddate (Union[Unset, int]):
        lastupdate (Union[Unset, int]):
        offset (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MeasureGetmeasResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        meastype=meastype,
        meastypes=meastypes,
        category=category,
        startdate=startdate,
        enddate=enddate,
        lastupdate=lastupdate,
        offset=offset,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    meastype: Union[Unset, int] = UNSET,
    meastypes: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
    startdate: Union[Unset, int] = UNSET,
    enddate: Union[Unset, int] = UNSET,
    lastupdate: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[MeasureGetmeasResponse200]:
    """Measure  - Getmeas

     Provides measures stored at a specific date among the types below. Please refer to the following
    responses for details.

    Args:
        action (str):
        meastype (Union[Unset, int]):
        meastypes (Union[Unset, str]):
        category (Union[Unset, int]):
        startdate (Union[Unset, int]):
        enddate (Union[Unset, int]):
        lastupdate (Union[Unset, int]):
        offset (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MeasureGetmeasResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        meastype=meastype,
        meastypes=meastypes,
        category=category,
        startdate=startdate,
        enddate=enddate,
        lastupdate=lastupdate,
        offset=offset,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    meastype: Union[Unset, int] = UNSET,
    meastypes: Union[Unset, str] = UNSET,
    category: Union[Unset, int] = UNSET,
    startdate: Union[Unset, int] = UNSET,
    enddate: Union[Unset, int] = UNSET,
    lastupdate: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[MeasureGetmeasResponse200]:
    """Measure  - Getmeas

     Provides measures stored at a specific date among the types below. Please refer to the following
    responses for details.

    Args:
        action (str):
        meastype (Union[Unset, int]):
        meastypes (Union[Unset, str]):
        category (Union[Unset, int]):
        startdate (Union[Unset, int]):
        enddate (Union[Unset, int]):
        lastupdate (Union[Unset, int]):
        offset (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MeasureGetmeasResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            meastype=meastype,
            meastypes=meastypes,
            category=category,
            startdate=startdate,
            enddate=enddate,
            lastupdate=lastupdate,
            offset=offset,
            authorization=authorization,
        )
    ).parsed
