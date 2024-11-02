from __future__ import annotations

import logging

from pytwitter import Api


def fetch_twitter_user_home_timelines(access_token: str, account_id: str):
    try:
        api = Api(bearer_token=access_token)
        response = api.get_timelines(user_id=account_id)
        home_timelines = response.data

        result = []
        for home_timeline in home_timelines:
            result.append({"tweet_id": home_timeline.id, "text": home_timeline.text})
    except Exception as e:
        logging.error(f"Fail to get timeline data from user_id={account_id}. error={e}")
        return []

    return result


def fetch_twitter_home_timelines(twitter_users):
    home_timelines = []
    for twitter_user in twitter_users:
        access_token = twitter_user.get("access_token")
        account_id = twitter_user.get("provider_account_id")
        timelines = fetch_twitter_user_home_timelines(access_token, account_id)
        home_timelines.append({"account_id": account_id, "timelines": timelines})
    return home_timelines
