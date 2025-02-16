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


class Withings(client.AuthenticatedClient):
    def __init__(self, access_token: Oauth2GetaccesstokenResponse200Body) -> None:
        self.__access_token = access_token
        client.AuthenticatedClient.__init__(  # type: ignore
            self,
            token=cast(str, access_token.access_token),
            base_url=constants.BASE_URL,
        )

    def wrap(self, fn: Callable[P, R]):
        refresh, _ = auth.needs_refreshing(self.__access_token)
        if refresh:
            self.__access_token = auth.refresh_access_token(self.__access_token)
        return functools.partial(
            fn,
            client=self,
            authorization=f"Bearer {self.__access_token.access_token}",
        )

    @staticmethod
    def from_local() -> "Withings":
        return Withings(auth.get_access_token())
