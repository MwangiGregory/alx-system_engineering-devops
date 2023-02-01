#!/usr/bin/python3
"""
Contains function top_ten
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of
     the first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': "My user agent 1.0"}
    payload = {'limit': 10}
    res = requests.get(
                       url, allow_redirects=False,
                       headers=headers,
                       params=payload)
    hot_posts = res.json()['data']['children']
    for post in hot_posts:
        post_title = post['data']['title']
        print(post_title)
