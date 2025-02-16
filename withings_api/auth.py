"""Helper utilities for OAuth2 flow."""

from contextvars import ContextVar
import datetime
import json
import logging
import os
import secrets
import threading
from typing import Literal, Sequence, TypeAlias, TypedDict, cast

import requests
from withings_api import constants
import urllib.parse
import webbrowser
from http import server

from withings_api.models.oauth_2_getaccesstoken_response_200_body import (
    Oauth2GetaccesstokenResponse200Body,
)

Scope: TypeAlias = Literal[
    "user.info", "user.metrics", "user.activity", "user.sleepevents"
]
REDIRECT_LOCALLY = constants.REDIRECT_URI.startswith(
    "http://localhost:"
) or constants.REDIRECT_URI.startswith("http://127.0.0.1:")

TOKEN_URL = "https://wbsapi.withings.net/v2/oauth2"
TOKEN_SAVE_PATH = os.path.expanduser("~/withings.config.json")

logger = logging.getLogger(__name__)


class Oauth2Context(TypedDict):
    """Description of thread local context."""

    request_started_at: datetime.datetime


context: ContextVar[Oauth2Context] = ContextVar("withings_oauth2")


def create_local_client() -> str | None:
    """Spin up a local client to use as the redirect_uri target."""
    logger = logging.getLogger(__name__)
    host = urllib.parse.urlparse(constants.REDIRECT_URI)
    address, port = host.netloc.split(":", maxsplit=1)
    code = None

    class AuthClient(server.BaseHTTPRequestHandler):
        def do_GET(self):
            path = urllib.parse.urlsplit(self.path)
            if path.netloc not in ("/", ""):
                self.send_error(404)
                return
            try:
                nonlocal code
                query = urllib.parse.parse_qs(path.query)
                if "code" not in query:
                    return self.send_error(
                        422, explain="Response must contain a code query parameter."
                    )
                code = query["code"][0]
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(
                    bytes(
                        """<html>
    <head>
        
    </head>
    <body>You can now close this tab...
        <script type='text/javascript'>
                window.opener && window.opener.location.reload(true);
                window.close();
        </script>
    </body>
</html>""",
                        "utf-8",
                    )
                )
            except Exception as e:
                logger.exception(e)
                self.send_error(500)
            finally:
                server_closer = threading.Thread(
                    target=tmp_server.shutdown, daemon=True
                )
                server_closer.start()

    tmp_server = server.HTTPServer((address, int(port)), AuthClient)
    tmp_server.serve_forever()
    return code


def get_auth_url(
    state: str,
    scopes: Sequence[Scope],
    redirect_uri: str = constants.REDIRECT_URI,
    client_id: str = constants.CLIENT_ID,
):
    """Get the authentication URL."""
    return f"https://account.withings.com/oauth2_user/authorize2?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&state={state}&scope={','.join(scopes)}"


def init_auth_flow_locally(
    open_browser: bool = True,
    scopes: Sequence[Scope] = (
        "user.info",
        "user.metrics",
        "user.activity",
        "user.sleepevents",
    ),
    client_id: str = constants.CLIENT_ID,
    client_secret: str = constants.CLIENT_SECRET,
    redirect_uri: str = constants.REDIRECT_URI,
    save_location: str = TOKEN_SAVE_PATH,
):
    """Initialize the OAuth2 flow."""
    if not REDIRECT_LOCALLY:
        raise RuntimeError("redirect uri must be localhost or 127.0.0.1")
    state = secrets.token_urlsafe()
    auth_url = get_auth_url(
        redirect_uri=redirect_uri, state=state, scopes=scopes, client_id=client_id
    )
    if open_browser:
        webbrowser.open(auth_url)
    code = cast(str, create_local_client())
    return get_access_token_from_code(
        code,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        save_location=save_location,
    )


def _save_response(
    response: requests.Response,
    save_location: str = TOKEN_SAVE_PATH,
):
    request_start_time = context.get()["request_started_at"]
    response.raise_for_status()
    data = response.json()["body"]

    with open(save_location, "w") as fp:
        json.dump({**data, "request_start_time": request_start_time}, fp, default=str)
    response_body = Oauth2GetaccesstokenResponse200Body.from_dict(data)
    logger.info(
        f"New token saved. Expires at ~{request_start_time + datetime.timedelta(seconds=cast(int, response_body.expires_in))}"
    )
    return response_body


def get_access_token_from_code(
    code: str,
    client_id: str = constants.CLIENT_ID,
    client_secret: str = constants.CLIENT_SECRET,
    redirect_uri: str = constants.REDIRECT_URI,
    save_location: str = TOKEN_SAVE_PATH,
):
    """Convert the code from the redirect URI to an access token."""
    context.set(Oauth2Context(request_started_at=datetime.datetime.now()))
    response = requests.post(
        TOKEN_URL,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        },
        data={
            "action": "requesttoken",
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
        },
        timeout=2.0,
    )
    return _save_response(response, save_location)


def refresh_access_token(
    refresh_token: str | Oauth2GetaccesstokenResponse200Body,
    client_id: str = constants.CLIENT_ID,
    client_secret: str = constants.CLIENT_SECRET,
    save_location: str = TOKEN_SAVE_PATH,
):
    """Refresh an access token."""
    context.set(Oauth2Context(request_started_at=datetime.datetime.now()))
    response = requests.post(
        TOKEN_URL,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        },
        data={
            "action": "requesttoken",
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
            if isinstance(refresh_token, str)
            else refresh_token.refresh_token,
        },
        timeout=2.0,
    )
    return _save_response(response, save_location)


def needs_refreshing(
    oauth2_token: Oauth2GetaccesstokenResponse200Body, grace_period_s: int = 0
):
    """Check if a token needs refreshing."""
    request_start_time = oauth2_token.additional_properties.get("request_start_time")
    if request_start_time is None:
        return None, None

    expires_at = datetime.datetime.fromisoformat(
        request_start_time
    ) + datetime.timedelta(seconds=cast(int, oauth2_token.expires_in))
    return (expires_at - datetime.datetime.now()).seconds >= grace_period_s, expires_at


def get_access_token(
    client_id: str = constants.CLIENT_ID,
    client_secret: str = constants.CLIENT_SECRET,
    save_location: str = TOKEN_SAVE_PATH,
):
    """Get the currently stored access token."""
    try:
        with open(save_location) as fp:
            saved_token = Oauth2GetaccesstokenResponse200Body.from_dict(json.load(fp))
        refresh, expires_at = needs_refreshing(saved_token)
        if refresh:
            return refresh_access_token(
                refresh_token=saved_token,
                client_id=client_id,
                client_secret=client_secret,
                save_location=save_location,
            )
        logger.debug(f"Loaded token that expires @ ~{expires_at}.")
        return saved_token
    except FileNotFoundError as e:
        if not REDIRECT_LOCALLY:
            raise e
        logger.debug(e)
        return init_auth_flow_locally()
