from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.userv_2_get_response_200 import Userv2GetResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: str,
    client_id: str,
    nonce: str,
    signature: str,
    email: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["client_id"] = client_id

    params["nonce"] = nonce

    params["signature"] = signature

    params["email"] = email

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/user",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Userv2GetResponse200]:
    if response.status_code == 200:
        response_200 = Userv2GetResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Userv2GetResponse200]:
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
    nonce: str,
    signature: str,
    email: str,
) -> Response[Userv2GetResponse200]:
    """User v2  - Get

     Returns user information.

    **For data privacy reasons, this webservice is only available for integration solutions for which
    the provider is responsible for the account creation (ie Withings Cellular Solutions and Withings
    Mobile SDK integrations).**
    **This webservice will return an error the above condition is not met.**

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Userv2GetResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        nonce=nonce,
        signature=signature,
        email=email,
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
    nonce: str,
    signature: str,
    email: str,
) -> Optional[Userv2GetResponse200]:
    """User v2  - Get

     Returns user information.

    **For data privacy reasons, this webservice is only available for integration solutions for which
    the provider is responsible for the account creation (ie Withings Cellular Solutions and Withings
    Mobile SDK integrations).**
    **This webservice will return an error the above condition is not met.**

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Userv2GetResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        client_id=client_id,
        nonce=nonce,
        signature=signature,
        email=email,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    nonce: str,
    signature: str,
    email: str,
) -> Response[Userv2GetResponse200]:
    """User v2  - Get

     Returns user information.

    **For data privacy reasons, this webservice is only available for integration solutions for which
    the provider is responsible for the account creation (ie Withings Cellular Solutions and Withings
    Mobile SDK integrations).**
    **This webservice will return an error the above condition is not met.**

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Userv2GetResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        nonce=nonce,
        signature=signature,
        email=email,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    nonce: str,
    signature: str,
    email: str,
) -> Optional[Userv2GetResponse200]:
    """User v2  - Get

     Returns user information.

    **For data privacy reasons, this webservice is only available for integration solutions for which
    the provider is responsible for the account creation (ie Withings Cellular Solutions and Withings
    Mobile SDK integrations).**
    **This webservice will return an error the above condition is not met.**

    Args:
        action (str):
        client_id (str):
        nonce (str):
        signature (str):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Userv2GetResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            client_id=client_id,
            nonce=nonce,
            signature=signature,
            email=email,
        )
    ).parsed
