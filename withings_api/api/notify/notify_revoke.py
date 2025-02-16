from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notify_revoke_response_200 import NotifyRevokeResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    callbackurl: str,
    appli: Union[Unset, int] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["callbackurl"] = callbackurl

    params["appli"] = appli

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/notify",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[NotifyRevokeResponse200]:
    if response.status_code == 200:
        response_200 = NotifyRevokeResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NotifyRevokeResponse200]:
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
    callbackurl: str,
    appli: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[NotifyRevokeResponse200]:
    """Notify  - Revoke

     Disables all notifications for a given user.

    Args:
        action (str):
        callbackurl (str):
        appli (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotifyRevokeResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        callbackurl=callbackurl,
        appli=appli,
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
    callbackurl: str,
    appli: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[NotifyRevokeResponse200]:
    """Notify  - Revoke

     Disables all notifications for a given user.

    Args:
        action (str):
        callbackurl (str):
        appli (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotifyRevokeResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        callbackurl=callbackurl,
        appli=appli,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    callbackurl: str,
    appli: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[NotifyRevokeResponse200]:
    """Notify  - Revoke

     Disables all notifications for a given user.

    Args:
        action (str):
        callbackurl (str):
        appli (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotifyRevokeResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        callbackurl=callbackurl,
        appli=appli,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    callbackurl: str,
    appli: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[NotifyRevokeResponse200]:
    """Notify  - Revoke

     Disables all notifications for a given user.

    Args:
        action (str):
        callbackurl (str):
        appli (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotifyRevokeResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            callbackurl=callbackurl,
            appli=appli,
            authorization=authorization,
        )
    ).parsed
