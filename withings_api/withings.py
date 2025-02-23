import functools
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
    cast,
)

import requests
from withings_api import auth, client, constants
from withings_api.models.oauth_2_getaccesstoken_response_200_body import (
    Oauth2GetaccesstokenResponse200Body,
)

P = ParamSpec("P")
R = TypeVar("R", covariant=True)


def create_api_wrapper(_access_token: Oauth2GetaccesstokenResponse200Body):
    access_token = _access_token
    withings_client = client.AuthenticatedClient(  # type: ignore
        token=cast(str, access_token.access_token),
        base_url=constants.BASE_URL,
    )

    def wrap(fn: Callable[P, R]):
        nonlocal access_token
        refresh, _ = auth.needs_refreshing(access_token)
        if refresh:
            access_token = auth.refresh_access_token(access_token)
        return functools.partial(
            fn,
            client=withings_client,
            authorization=f"Bearer {access_token.access_token}",
        )

    return wrap


def create_local_api_wrapper():
    return create_api_wrapper(auth.get_access_token())


def subscribe_to_notifications(
    _access_token: Oauth2GetaccesstokenResponse200Body, appli: int = 1, *, url: str
):
    """Subscribe to notifications.

    See https://developer.withings.com/developer-guide/v3/data-api/keep-user-data-up-to-date/#notification-categories for information about appli."""
    access_token = _access_token
    refresh, _ = auth.needs_refreshing(access_token)
    if refresh:
        access_token = auth.refresh_access_token(access_token)
    data: dict[str, str | int] = {
        "action": "subscribe",
        "callbackurl": url,
        "appli": appli,
    }
    response = requests.post(
        "https://wbsapi.withings.net",
        json=data,
        headers={
            "authorization": f"Bearer {access_token.access_token}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    response.raise_for_status()
    return response
