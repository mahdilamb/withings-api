import json
import os
import dotenv


dotenv.load_dotenv()

CLIENT_ID: str = os.getenv("WITHINGS_CLIENT_ID")  # type: ignore
CLIENT_SECRET: str = os.getenv("WITHINGS_CLIENT_SECRET")  # type: ignore
REDIRECT_URI: str = os.getenv("WITHINGS_REDIRECT_URI")  # type: ignore
BASE_URL = "https://wbsapi.withings.net"
if (json_path := os.getenv("WITHINGS_CONFIG_JSON")) and os.path.exists(json_path):
    with open(json_path, "r") as fp:
        data = json.load(fp)
    CLIENT_ID = data["client_id"]  # type: ignore
    CLIENT_SECRET = data["client_secret"]  # type: ignore
    REDIRECT_URI = data["redirect_uri"]  # type: ignore

if None in (CLIENT_ID, CLIENT_SECRET, REDIRECT_URI):  # type: ignore
    raise RuntimeError(
        "Ensure that either `WITHINGS_CLIENT_ID`, `WITHINGS_CLIENT_SECRET`, `WITHINGS_REDIRECT_URI` are set or are stored in a json file located at `WITHINGS_CONFIG_JSON`, with the attributes: `client_id`, `client_secret`, `redirect_uri`."
    )
