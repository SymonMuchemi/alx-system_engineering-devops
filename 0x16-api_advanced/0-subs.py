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

    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Custom'}

    try:
        response = requests.get(url=base_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:
            print(f"The {subreddit} subreddit doesn't exist")
            return 0
        else:
            print(f"An error occured with code: {response.status_code}")
            return 0
    except requests.RequestException as e:
        print(f'An error occured: {e}')
        return 0

