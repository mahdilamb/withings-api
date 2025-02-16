from enum import Enum


class TokenRequestWithClientSecretGrantType(str, Enum):
    AUTHORIZATION_CODE = "authorization_code"

    def __str__(self) -> str:
        return str(self.value)
