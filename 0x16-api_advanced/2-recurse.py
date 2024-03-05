#!/usr/bin/python3
""" Recurs it """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ top 10 hot articles in a subbreddit"""
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )
    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = req.json().get("data").get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
