#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers on a subreddit"""
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'Python/requests:APIproject:\
    v1.0.0 (by /u/smakosh)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
