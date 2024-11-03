from __future__ import annotations

import base64

import requests

from app.config import Config
from app.logger import logger


# retrieve user's access_token by refresh_token
def auth_user(refresh_token: str):
    auth_code = f"{Config.TWITTER_CLIENT_ID}:{Config.TWITTER_CLIENT_SECRET}"
    encoded_auth_code = base64.b64encode(auth_code.encode()).decode()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_auth_code}",
    }
    request_body = {
        "client_id": Config.TWITTER_CLIENT_ID,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }

    response = requests.post(
        "https://api.x.com/2/oauth2/token", headers=headers, data=request_body
    )

    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens.get("access_token")
        refresh_token = tokens.get("refresh_token")
        return [access_token, refresh_token]
    else:
        logger.warn(f"Fail to retrieve access_token")
        return ["", ""]