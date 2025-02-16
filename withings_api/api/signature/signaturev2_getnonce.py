from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.signaturev_2_getnonce_response_200 import Signaturev2GetnonceResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: str,
    client_id: str,
    timestamp: int,
    signature: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["client_id"] = client_id

    params["timestamp"] = timestamp

    params["signature"] = signature

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/signature",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Signaturev2GetnonceResponse200]:
    if response.status_code == 200:
        response_200 = Signaturev2GetnonceResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Signaturev2GetnonceResponse200]:
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
    timestamp: int,
    signature: str,
) -> Response[Signaturev2GetnonceResponse200]:
    """Signature v2  - Getnonce

     A ```nonce``` is a random token that is generated and stored in Withings server with **30 minutes of
    validity**.

    As a partner, you will use this ```nonce``` token in the API services that require a ```signature```
    so that Withings can check that the ```nonce``` token is still valid and was never used before. The
    usage of a ```nonce``` token prevents your service calls from replay attacks.

    Because this service is an Device Management service, Withings checks your authorized access using
    your ```client_id``` and your ```secret``` based ```signature```.

    To generate the ```signature``` please follow these steps:

    - Sort the following parameters alphabetically:
        - ```action```
        - ```client_id```
        - ```timestamp```
    - Generate a string by concatenating values separated by a comma. The string should look like:
    *value1,value2,value3*.
    - Apply a hmac hashing function on the string using the algorithm ```sha256``` and your partner
    ```client_secret```  (available in your [Withings partner
    dashboard](https://developer.withings.com/dashboard/)) as a secret key.
    - Add the hash string in the parameters under the key ```signature```

    Args:
        action (str):
        client_id (str):
        timestamp (int):
        signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Signaturev2GetnonceResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        timestamp=timestamp,
        signature=signature,
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
    timestamp: int,
    signature: str,
) -> Optional[Signaturev2GetnonceResponse200]:
    """Signature v2  - Getnonce

     A ```nonce``` is a random token that is generated and stored in Withings server with **30 minutes of
    validity**.

    As a partner, you will use this ```nonce``` token in the API services that require a ```signature```
    so that Withings can check that the ```nonce``` token is still valid and was never used before. The
    usage of a ```nonce``` token prevents your service calls from replay attacks.

    Because this service is an Device Management service, Withings checks your authorized access using
    your ```client_id``` and your ```secret``` based ```signature```.

    To generate the ```signature``` please follow these steps:

    - Sort the following parameters alphabetically:
        - ```action```
        - ```client_id```
        - ```timestamp```
    - Generate a string by concatenating values separated by a comma. The string should look like:
    *value1,value2,value3*.
    - Apply a hmac hashing function on the string using the algorithm ```sha256``` and your partner
    ```client_secret```  (available in your [Withings partner
    dashboard](https://developer.withings.com/dashboard/)) as a secret key.
    - Add the hash string in the parameters under the key ```signature```

    Args:
        action (str):
        client_id (str):
        timestamp (int):
        signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Signaturev2GetnonceResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        client_id=client_id,
        timestamp=timestamp,
        signature=signature,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    timestamp: int,
    signature: str,
) -> Response[Signaturev2GetnonceResponse200]:
    """Signature v2  - Getnonce

     A ```nonce``` is a random token that is generated and stored in Withings server with **30 minutes of
    validity**.

    As a partner, you will use this ```nonce``` token in the API services that require a ```signature```
    so that Withings can check that the ```nonce``` token is still valid and was never used before. The
    usage of a ```nonce``` token prevents your service calls from replay attacks.

    Because this service is an Device Management service, Withings checks your authorized access using
    your ```client_id``` and your ```secret``` based ```signature```.

    To generate the ```signature``` please follow these steps:

    - Sort the following parameters alphabetically:
        - ```action```
        - ```client_id```
        - ```timestamp```
    - Generate a string by concatenating values separated by a comma. The string should look like:
    *value1,value2,value3*.
    - Apply a hmac hashing function on the string using the algorithm ```sha256``` and your partner
    ```client_secret```  (available in your [Withings partner
    dashboard](https://developer.withings.com/dashboard/)) as a secret key.
    - Add the hash string in the parameters under the key ```signature```

    Args:
        action (str):
        client_id (str):
        timestamp (int):
        signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Signaturev2GetnonceResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        client_id=client_id,
        timestamp=timestamp,
        signature=signature,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    client_id: str,
    timestamp: int,
    signature: str,
) -> Optional[Signaturev2GetnonceResponse200]:
    """Signature v2  - Getnonce

     A ```nonce``` is a random token that is generated and stored in Withings server with **30 minutes of
    validity**.

    As a partner, you will use this ```nonce``` token in the API services that require a ```signature```
    so that Withings can check that the ```nonce``` token is still valid and was never used before. The
    usage of a ```nonce``` token prevents your service calls from replay attacks.

    Because this service is an Device Management service, Withings checks your authorized access using
    your ```client_id``` and your ```secret``` based ```signature```.

    To generate the ```signature``` please follow these steps:

    - Sort the following parameters alphabetically:
        - ```action```
        - ```client_id```
        - ```timestamp```
    - Generate a string by concatenating values separated by a comma. The string should look like:
    *value1,value2,value3*.
    - Apply a hmac hashing function on the string using the algorithm ```sha256``` and your partner
    ```client_secret```  (available in your [Withings partner
    dashboard](https://developer.withings.com/dashboard/)) as a secret key.
    - Add the hash string in the parameters under the key ```signature```

    Args:
        action (str):
        client_id (str):
        timestamp (int):
        signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Signaturev2GetnonceResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            client_id=client_id,
            timestamp=timestamp,
            signature=signature,
        )
    ).parsed
