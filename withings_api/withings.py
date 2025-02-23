import functools
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
    cast,
)
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
