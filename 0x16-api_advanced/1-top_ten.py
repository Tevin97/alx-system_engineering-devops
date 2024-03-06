#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    for a given subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None

    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyAPIAgent"}  # Set a custom User-Agent header

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts[:10]:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)  # Invalid subreddit or request failed
