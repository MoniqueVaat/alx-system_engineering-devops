#!/usr/bin/python3
""" retrieve titles for posts from reddit api """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """return list of all host posts titles of a subreddit """

    headers = {'User-agent': 'my agent'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=70&after={}".format(
	   subreddit, after)
    posts = requests.get(url, headers=headers, allow_redirects=False)

    if posts.status_code == 200:
        posts = posts.json()['data']
        after = posts['after']
        posts = posts['children']
        for posts in posts:
	    hot-list.append(post['data']['title'])
	if after is not None:
	    recurse(subreddit, hot_list, after)
	return (hot_list)
    else:
	return (None)
