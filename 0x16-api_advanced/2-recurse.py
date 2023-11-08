#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
 a list containing the titles of all hot articles for a given subreddit. """

import requests

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyAPIAgent"}  # Set a custom User-Agent header
    params = {"after": after} if after else None
    myRequest = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)

    if myRequest.status_code == 200:
        try:
            data = myRequest.json()
            posts = data["data"]["children"]

            for post in posts:
                title = post["data"]["title"]
                hot_list.append(title)

            after = data["data"]["after"]
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
    else:
        return None
