from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notify_list_response_200 import NotifyListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    appli: Union[Unset, int] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

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
) -> Optional[NotifyListResponse200]:
    if response.status_code == 200:
        response_200 = NotifyListResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NotifyListResponse200]:
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
    appli: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[NotifyListResponse200]:
    """Notify  - List

     Lists notification configuration for this user.

    Args:
        action (str):
        appli (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotifyListResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
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
    appli: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[NotifyListResponse200]:
    """Notify  - List

     Lists notification configuration for this user.

    Args:
        action (str):
        appli (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotifyListResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        appli=appli,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    appli: Union[Unset, int] = UNSET,
    authorization: str,
) -> Response[NotifyListResponse200]:
    """Notify  - List

     Lists notification configuration for this user.

    Args:
        action (str):
        appli (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotifyListResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        appli=appli,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    appli: Union[Unset, int] = UNSET,
    authorization: str,
) -> Optional[NotifyListResponse200]:
    """Notify  - List

     Lists notification configuration for this user.

    Args:
        action (str):
        appli (Union[Unset, int]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotifyListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            appli=appli,
            authorization=authorization,
        )
    ).parsed
