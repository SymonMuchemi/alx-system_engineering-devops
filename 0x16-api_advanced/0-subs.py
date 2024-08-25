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
    # https://www.reddit.com/r/programming/about.json
    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(
        base_url,
        headers={
            'User-Agent': 'My-User-Agent'
            },
        allow_redirects=False)
    
    # print(response.status_code)

    if response.status_code >= 300:
        return 0

    subs = response.json()
    n = subs.get('data').get('subscribers')

    return n
