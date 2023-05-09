#!/usr/bin/python3
""" 100-count.py """
import json
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """ prints a sorted count of given keywords """

    if counts is None:
        counts = {}

    if after is None:
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        for topic in data['data']['children']:
            title = topic['data']['title']
            words = [word.lower() for word in title.split()]
            for word in word_list:
                if word.lower() in words:
                    counts[word.lower()] += words.count(word.lower())

        if data['data']['after'] is not None:
            count_words(subreddit, word_list, data['data']['after'], counts)

    if after is None:
        counts = {k: v for k, v in counts.items() if v > 0}
        counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in counts:
            print("{}: {}".format(word, count))
