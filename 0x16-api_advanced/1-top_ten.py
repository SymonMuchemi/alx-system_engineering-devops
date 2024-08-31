#!/usr/bin/python3
"""
Quaries the Reddit API to get the titles of
the first 10 posts lidted for a given subreddit
"""
import requests


def top_ten(subreddit):
    response = requests.get(
        f'https://www.reddit.com/r/{subreddit}/hot.json',
        headers={'User-Agent': 'Custon'},
        params={'limit': 10}
    )

    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for item in data:
            print(item.get('data').get('title'))
    else:
        print(None)
