from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notify_subscribe_response_200 import NotifySubscribeResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    callbackurl: str,
    appli: int,
    signature: str,
    nonce: str,
    client_id: str,
    comment: Union[Unset, str] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["action"] = action

    params["callbackurl"] = callbackurl

    params["appli"] = appli

    params["signature"] = signature

    params["nonce"] = nonce

    params["client_id"] = client_id

    params["comment"] = comment

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
) -> Optional[NotifySubscribeResponse200]:
    if response.status_code == 200:
        response_200 = NotifySubscribeResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NotifySubscribeResponse200]:
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
    appli: int,
    signature: str,
    nonce: str,
    client_id: str,
    comment: Union[Unset, str] = UNSET,
    authorization: str,
) -> Response[NotifySubscribeResponse200]:
    """Notify  - Subscribe

     This service allows to receive notifications from Withings:

    - for the Health Data APIs : your application can subscribe to a variety or events, including user
    data  creation and updates. Notifications will be sent to your servers when the subscribed events
    occur. ([more information](/developer-guide/v3/data-api/keep-user-data-up-to-date)). Please note
    that you need to subscribe for each individual user.
    - for the Logistics APIs: a notification will be sent when there is an order update ([more
    information](developer-guide/v3/integration-guide/dropship-only/logistics-api/observe-order-
    updates))
    - for partners integrating Withings Cellular Solutions or Withings Mobile SDK: you can use the
    ```NO_ACCOUNT_ASSOCIATED``` event to track unassociated devices . Please note you need to subscribe
    only once per application.

    **Note**: depending on your use case, the request parameters may change:

    - for the Health Data APIs: use a valid ```access_token``` in the header but don't use
    ```signature``` and ```nonce``` in the query parameters.
    - for the Logistics APIs: the subscription is done automatically an order is placed (please refer to
    the [dedicated documentation section](developer-guide/v3/integration-guide/dropship-only/logistics-
    api/observe-order-updates#how-to-receive-order-update-notifications))
    - for partners integrating Withings Cellular Solutions or Withings Mobile SDK, to subscribe to the
    ```NO_ACCOUNT_ASSOCIATED``` event (appli = 53): use ```signature``` and ```nonce``` parameters but
    don't include an ```access_token``` in the header.

    Args:
        action (str):
        callbackurl (str):
        appli (int):
        signature (str):
        nonce (str):
        client_id (str):
        comment (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotifySubscribeResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        callbackurl=callbackurl,
        appli=appli,
        signature=signature,
        nonce=nonce,
        client_id=client_id,
        comment=comment,
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
    appli: int,
    signature: str,
    nonce: str,
    client_id: str,
    comment: Union[Unset, str] = UNSET,
    authorization: str,
) -> Optional[NotifySubscribeResponse200]:
    """Notify  - Subscribe

     This service allows to receive notifications from Withings:

    - for the Health Data APIs : your application can subscribe to a variety or events, including user
    data  creation and updates. Notifications will be sent to your servers when the subscribed events
    occur. ([more information](/developer-guide/v3/data-api/keep-user-data-up-to-date)). Please note
    that you need to subscribe for each individual user.
    - for the Logistics APIs: a notification will be sent when there is an order update ([more
    information](developer-guide/v3/integration-guide/dropship-only/logistics-api/observe-order-
    updates))
    - for partners integrating Withings Cellular Solutions or Withings Mobile SDK: you can use the
    ```NO_ACCOUNT_ASSOCIATED``` event to track unassociated devices . Please note you need to subscribe
    only once per application.

    **Note**: depending on your use case, the request parameters may change:

    - for the Health Data APIs: use a valid ```access_token``` in the header but don't use
    ```signature``` and ```nonce``` in the query parameters.
    - for the Logistics APIs: the subscription is done automatically an order is placed (please refer to
    the [dedicated documentation section](developer-guide/v3/integration-guide/dropship-only/logistics-
    api/observe-order-updates#how-to-receive-order-update-notifications))
    - for partners integrating Withings Cellular Solutions or Withings Mobile SDK, to subscribe to the
    ```NO_ACCOUNT_ASSOCIATED``` event (appli = 53): use ```signature``` and ```nonce``` parameters but
    don't include an ```access_token``` in the header.

    Args:
        action (str):
        callbackurl (str):
        appli (int):
        signature (str):
        nonce (str):
        client_id (str):
        comment (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotifySubscribeResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        callbackurl=callbackurl,
        appli=appli,
        signature=signature,
        nonce=nonce,
        client_id=client_id,
        comment=comment,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    callbackurl: str,
    appli: int,
    signature: str,
    nonce: str,
    client_id: str,
    comment: Union[Unset, str] = UNSET,
    authorization: str,
) -> Response[NotifySubscribeResponse200]:
    """Notify  - Subscribe

     This service allows to receive notifications from Withings:

    - for the Health Data APIs : your application can subscribe to a variety or events, including user
    data  creation and updates. Notifications will be sent to your servers when the subscribed events
    occur. ([more information](/developer-guide/v3/data-api/keep-user-data-up-to-date)). Please note
    that you need to subscribe for each individual user.
    - for the Logistics APIs: a notification will be sent when there is an order update ([more
    information](developer-guide/v3/integration-guide/dropship-only/logistics-api/observe-order-
    updates))
    - for partners integrating Withings Cellular Solutions or Withings Mobile SDK: you can use the
    ```NO_ACCOUNT_ASSOCIATED``` event to track unassociated devices . Please note you need to subscribe
    only once per application.

    **Note**: depending on your use case, the request parameters may change:

    - for the Health Data APIs: use a valid ```access_token``` in the header but don't use
    ```signature``` and ```nonce``` in the query parameters.
    - for the Logistics APIs: the subscription is done automatically an order is placed (please refer to
    the [dedicated documentation section](developer-guide/v3/integration-guide/dropship-only/logistics-
    api/observe-order-updates#how-to-receive-order-update-notifications))
    - for partners integrating Withings Cellular Solutions or Withings Mobile SDK, to subscribe to the
    ```NO_ACCOUNT_ASSOCIATED``` event (appli = 53): use ```signature``` and ```nonce``` parameters but
    don't include an ```access_token``` in the header.

    Args:
        action (str):
        callbackurl (str):
        appli (int):
        signature (str):
        nonce (str):
        client_id (str):
        comment (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotifySubscribeResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        callbackurl=callbackurl,
        appli=appli,
        signature=signature,
        nonce=nonce,
        client_id=client_id,
        comment=comment,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    callbackurl: str,
    appli: int,
    signature: str,
    nonce: str,
    client_id: str,
    comment: Union[Unset, str] = UNSET,
    authorization: str,
) -> Optional[NotifySubscribeResponse200]:
    """Notify  - Subscribe

     This service allows to receive notifications from Withings:

    - for the Health Data APIs : your application can subscribe to a variety or events, including user
    data  creation and updates. Notifications will be sent to your servers when the subscribed events
    occur. ([more information](/developer-guide/v3/data-api/keep-user-data-up-to-date)). Please note
    that you need to subscribe for each individual user.
    - for the Logistics APIs: a notification will be sent when there is an order update ([more
    information](developer-guide/v3/integration-guide/dropship-only/logistics-api/observe-order-
    updates))
    - for partners integrating Withings Cellular Solutions or Withings Mobile SDK: you can use the
    ```NO_ACCOUNT_ASSOCIATED``` event to track unassociated devices . Please note you need to subscribe
    only once per application.

    **Note**: depending on your use case, the request parameters may change:

    - for the Health Data APIs: use a valid ```access_token``` in the header but don't use
    ```signature``` and ```nonce``` in the query parameters.
    - for the Logistics APIs: the subscription is done automatically an order is placed (please refer to
    the [dedicated documentation section](developer-guide/v3/integration-guide/dropship-only/logistics-
    api/observe-order-updates#how-to-receive-order-update-notifications))
    - for partners integrating Withings Cellular Solutions or Withings Mobile SDK, to subscribe to the
    ```NO_ACCOUNT_ASSOCIATED``` event (appli = 53): use ```signature``` and ```nonce``` parameters but
    don't include an ```access_token``` in the header.

    Args:
        action (str):
        callbackurl (str):
        appli (int):
        signature (str):
        nonce (str):
        client_id (str):
        comment (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotifySubscribeResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            callbackurl=callbackurl,
            appli=appli,
            signature=signature,
            nonce=nonce,
            client_id=client_id,
            comment=comment,
            authorization=authorization,
        )
    ).parsed
