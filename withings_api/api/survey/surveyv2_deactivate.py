from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.surveyv_2_deactivate_response_200 import Surveyv2DeactivateResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    surveyid: str,
    userids: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["signature"] = signature

    params["client_id"] = client_id

    params["nonce"] = nonce

    params["surveyid"] = surveyid

    params["userids"] = userids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/survey",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Surveyv2DeactivateResponse200]:
    if response.status_code == 200:
        response_200 = Surveyv2DeactivateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Surveyv2DeactivateResponse200]:
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
    surveyid: str,
    userids: str,
) -> Response[Surveyv2DeactivateResponse200]:
    """Survey v2  - Deactivate

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        surveyid (str):
        userids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Surveyv2DeactivateResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        surveyid=surveyid,
        userids=userids,
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
    surveyid: str,
    userids: str,
) -> Optional[Surveyv2DeactivateResponse200]:
    """Survey v2  - Deactivate

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        surveyid (str):
        userids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Surveyv2DeactivateResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        surveyid=surveyid,
        userids=userids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    surveyid: str,
    userids: str,
) -> Response[Surveyv2DeactivateResponse200]:
    """Survey v2  - Deactivate

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        surveyid (str):
        userids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Surveyv2DeactivateResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        surveyid=surveyid,
        userids=userids,
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
    surveyid: str,
    userids: str,
) -> Optional[Surveyv2DeactivateResponse200]:
    """Survey v2  - Deactivate

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        surveyid (str):
        userids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Surveyv2DeactivateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            signature=signature,
            client_id=client_id,
            nonce=nonce,
            surveyid=surveyid,
            userids=userids,
        )
    ).parsed
