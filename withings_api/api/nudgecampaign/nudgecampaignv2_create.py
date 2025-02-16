from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nudgecampaignv_2_create_response_200 import Nudgecampaignv2CreateResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    nudgeid: int,
    startdate: int,
    enddate: int,
    max_display_count: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["signature"] = signature

    params["client_id"] = client_id

    params["nonce"] = nonce

    params["nudgeid"] = nudgeid

    params["startdate"] = startdate

    params["enddate"] = enddate

    params["max_display_count"] = max_display_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/nudgecampaign",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Nudgecampaignv2CreateResponse200]:
    if response.status_code == 200:
        response_200 = Nudgecampaignv2CreateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Nudgecampaignv2CreateResponse200]:
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
    signature: str,
    client_id: str,
    nonce: str,
    nudgeid: int,
    startdate: int,
    enddate: int,
    max_display_count: int,
) -> Response[Nudgecampaignv2CreateResponse200]:
    """Nudgecampaign v2  - Create

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        nudgeid (int):
        startdate (int):
        enddate (int):
        max_display_count (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Nudgecampaignv2CreateResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        nudgeid=nudgeid,
        startdate=startdate,
        enddate=enddate,
        max_display_count=max_display_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    nudgeid: int,
    startdate: int,
    enddate: int,
    max_display_count: int,
) -> Optional[Nudgecampaignv2CreateResponse200]:
    """Nudgecampaign v2  - Create

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        nudgeid (int):
        startdate (int):
        enddate (int):
        max_display_count (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Nudgecampaignv2CreateResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        nudgeid=nudgeid,
        startdate=startdate,
        enddate=enddate,
        max_display_count=max_display_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    nudgeid: int,
    startdate: int,
    enddate: int,
    max_display_count: int,
) -> Response[Nudgecampaignv2CreateResponse200]:
    """Nudgecampaign v2  - Create

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        nudgeid (int):
        startdate (int):
        enddate (int):
        max_display_count (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Nudgecampaignv2CreateResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        nudgeid=nudgeid,
        startdate=startdate,
        enddate=enddate,
        max_display_count=max_display_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    nudgeid: int,
    startdate: int,
    enddate: int,
    max_display_count: int,
) -> Optional[Nudgecampaignv2CreateResponse200]:
    """Nudgecampaign v2  - Create

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        nudgeid (int):
        startdate (int):
        enddate (int):
        max_display_count (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Nudgecampaignv2CreateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            signature=signature,
            client_id=client_id,
            nonce=nonce,
            nudgeid=nudgeid,
            startdate=startdate,
            enddate=enddate,
            max_display_count=max_display_count,
        )
    ).parsed
