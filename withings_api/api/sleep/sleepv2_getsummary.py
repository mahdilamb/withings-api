from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    startdateymd: str,
    enddateymd: str,
    lastupdate: int,
    data_fields: Union[Unset, str] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["startdateymd"] = startdateymd

    params["enddateymd"] = enddateymd

    params["lastupdate"] = lastupdate

    params["data_fields"] = data_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/sleep",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    startdateymd: str,
    enddateymd: str,
    lastupdate: int,
    data_fields: Union[Unset, str] = UNSET,
    authorization: str,
) -> Response[Any]:
    """Sleep v2  - Getsummary

     Returns sleep activity summaries, which are an aggregation of all the data captured at high
    frequency during the sleep activity.

    Use the [Sleep v2 - Get](#operation/sleepv2-get) service to get the high frequency data used to
    build these summaries.

    Args:
        action (str):
        startdateymd (str):
        enddateymd (str):
        lastupdate (int):
        data_fields (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        action=action,
        startdateymd=startdateymd,
        enddateymd=enddateymd,
        lastupdate=lastupdate,
        data_fields=data_fields,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    startdateymd: str,
    enddateymd: str,
    lastupdate: int,
    data_fields: Union[Unset, str] = UNSET,
    authorization: str,
) -> Response[Any]:
    """Sleep v2  - Getsummary

     Returns sleep activity summaries, which are an aggregation of all the data captured at high
    frequency during the sleep activity.

    Use the [Sleep v2 - Get](#operation/sleepv2-get) service to get the high frequency data used to
    build these summaries.

    Args:
        action (str):
        startdateymd (str):
        enddateymd (str):
        lastupdate (int):
        data_fields (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        action=action,
        startdateymd=startdateymd,
        enddateymd=enddateymd,
        lastupdate=lastupdate,
        data_fields=data_fields,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
