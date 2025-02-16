from enum import Enum


class Dropshipmentv2GetorderstatusEnrich(str, Enum):
    F = "f"
    T = "t"

    def __str__(self) -> str:
        return str(self.value)
