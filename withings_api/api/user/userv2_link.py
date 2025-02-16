from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.userv_2_link_response_200 import Userv2LinkResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: str,
    mac_addresses: str,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["mac_addresses"] = mac_addresses

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/user",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Userv2LinkResponse200]:
    if response.status_code == 200:
        response_200 = Userv2LinkResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Userv2LinkResponse200]:
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
    mac_addresses: str,
    authorization: str,
) -> Response[Userv2LinkResponse200]:
    """User v2  - Link

     Links the devices related to the provided ```mac_addresses``` and the user related to the provided
    ```access_token```. If a cellular device is listed in the ```mac_address``` field, it will activate
    this device's cellular service and invoicing.

    **Important**:

    - Please note that the devices need to be authorized to be linked by API by the Partner. Please
    [contact Withings](mailto:partner-api@withings.com) for more information on device authorization.

    Args:
        action (str):
        mac_addresses (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Userv2LinkResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        mac_addresses=mac_addresses,
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
    mac_addresses: str,
    authorization: str,
) -> Optional[Userv2LinkResponse200]:
    """User v2  - Link

     Links the devices related to the provided ```mac_addresses``` and the user related to the provided
    ```access_token```. If a cellular device is listed in the ```mac_address``` field, it will activate
    this device's cellular service and invoicing.

    **Important**:

    - Please note that the devices need to be authorized to be linked by API by the Partner. Please
    [contact Withings](mailto:partner-api@withings.com) for more information on device authorization.

    Args:
        action (str):
        mac_addresses (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Userv2LinkResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        mac_addresses=mac_addresses,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    mac_addresses: str,
    authorization: str,
) -> Response[Userv2LinkResponse200]:
    """User v2  - Link

     Links the devices related to the provided ```mac_addresses``` and the user related to the provided
    ```access_token```. If a cellular device is listed in the ```mac_address``` field, it will activate
    this device's cellular service and invoicing.

    **Important**:

    - Please note that the devices need to be authorized to be linked by API by the Partner. Please
    [contact Withings](mailto:partner-api@withings.com) for more information on device authorization.

    Args:
        action (str):
        mac_addresses (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Userv2LinkResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        mac_addresses=mac_addresses,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    mac_addresses: str,
    authorization: str,
) -> Optional[Userv2LinkResponse200]:
    """User v2  - Link

     Links the devices related to the provided ```mac_addresses``` and the user related to the provided
    ```access_token```. If a cellular device is listed in the ```mac_address``` field, it will activate
    this device's cellular service and invoicing.

    **Important**:

    - Please note that the devices need to be authorized to be linked by API by the Partner. Please
    [contact Withings](mailto:partner-api@withings.com) for more information on device authorization.

    Args:
        action (str):
        mac_addresses (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Userv2LinkResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            mac_addresses=mac_addresses,
            authorization=authorization,
        )
    ).parsed
