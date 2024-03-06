#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
             Returns 0 if the subreddit is invalid.

    Raises:
        Exception: If the request to the API fails.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyAPIAgent"}  # Set a custom User-Agent header

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    elif response.status_code == 404:
        return 0  # Invalid subreddit
    else:
        raise Exception(f"Request failed status code {response.status_code}")
