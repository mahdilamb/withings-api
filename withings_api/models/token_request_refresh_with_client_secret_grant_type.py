from enum import Enum


class TokenRequestRefreshWithClientSecretGrantType(str, Enum):
    REFRESH_TOKEN = "refresh_token"

    def __str__(self) -> str:
        return str(self.value)
