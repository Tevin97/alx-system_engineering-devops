#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
 a list containing the titles of all hot articles for a given subreddit. """

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves the titles of all hot articles
    for a given subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of
        hot articles (default is an empty list).

    Returns:
        list: A list containing the titles of all hot articles.
        If no results are found, it returns None.

    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyAPIAgent"}  # Set a custom User-Agent header

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        # Check if there is a next page
        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    else:
        return None  # Invalid subreddit or request failed
