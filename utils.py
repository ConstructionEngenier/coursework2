import json
import pprint


def data_load(link):
    with open(link, "r") as fp:
        data = json.load(fp)
    return data


def get_posts():
    posts = data_load("data/data.json")
    return posts


def get_post_by_pk(post_pk):
    posts = data_load("data/data.json")
    for post in posts:
        if post["pk"] == post_pk:
            return post
    return None