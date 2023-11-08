#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API, parses the titles
    of all hot articles, and prints a sorted count of given
    keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): A token used for pagination
            (default is None).
        counts (dict): A dictionary to store the counts
            of each keyword (default is an empty dictionary).

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyAPIAgent"}  # Set a custom User-Agent header
    params = {"after": after} if after else None

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making a request: {e}")
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()

        for word in word_list:
            # Skip words with no matches
            if word not in counts and title.count(word.lower()):
                counts[word] = counts.get(word, 0) + title.count(word.lower())

    after = data.get("data", {}).get("after")

    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        print_counts(counts)


def print_counts(counts):
    """
    Prints the sorted count of keywords.

    Args:
        counts (dict): A dictionary containing the counts
            of each keyword.

    Returns:
        None
    """
    sorted_counts = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    for word, count in sorted_counts:
        print(f"{word}: {count}")
