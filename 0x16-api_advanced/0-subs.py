#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """fetch number of subcribers on a subreddit

    Args:
        subreddit (str): subreddit name

    Returns:
        int: number of subscribers
    """
    base_url = 'https://www.reddit.com/r/'
    response = requests.get(
        f'{base_url}{subreddit}/about.json',
        headers={
            'User-Agent': 'My-User-Agent'
            },
        allow_redirects=False)

    subs = response.json()
    n = subs.get('data').get('subscribers')

    return n
