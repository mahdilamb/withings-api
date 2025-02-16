"""A client library for accessing Withings developer documentation"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
__version__ = "0.1.1"