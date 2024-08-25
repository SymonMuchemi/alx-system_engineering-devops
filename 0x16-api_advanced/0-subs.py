#!/usr/bin/python3
"""get subreddit data"""
import requests


def number_of_subscribers(subreddit):
    """fetch number of subcribers on a subreddit

    Args:
        subreddit (str): subreddit name

    Returns:
        int: number of subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # https://www.reddit.com/r/programming/about.json
    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(
        base_url,
        headers={'User-Agent': 'Muchemis-Pc'},
        allow_redirects=False
    )

    if response.status_code >= 300:
        return 0

    try:
        subs = response.json()
        return subs.get('data').get('subscribers')
    except Exception:
        return 0
