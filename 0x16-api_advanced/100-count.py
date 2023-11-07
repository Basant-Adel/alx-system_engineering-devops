#!/usr/bin/python3
""" Write recursive to query Reddit API, title of all hot articles """
import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """ Print sorted count of given keywords """
    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))

        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    red = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(red, headers=header, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        rejs = response.json()['data']['children']
        reaft = response.json()['data']['after']

        for post in rejs:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, reaft, word_dict)
