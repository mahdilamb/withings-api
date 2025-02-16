from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    surveyid: str,
    lang: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["action"] = action

    params["signature"] = signature

    params["client_id"] = client_id

    params["nonce"] = nonce

    params["surveyid"] = surveyid

    params["lang"] = lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/survey",
        "params": params,
    }

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
    signature: str,
    client_id: str,
    nonce: str,
    surveyid: str,
    lang: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Survey v2  - Get

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        surveyid (str):
        lang (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        surveyid=surveyid,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    action: str,
    signature: str,
    client_id: str,
    nonce: str,
    surveyid: str,
    lang: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Survey v2  - Get

    Args:
        action (str):
        signature (str):
        client_id (str):
        nonce (str):
        surveyid (str):
        lang (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        action=action,
        signature=signature,
        client_id=client_id,
        nonce=nonce,
        surveyid=surveyid,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
