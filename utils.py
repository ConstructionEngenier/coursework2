import json
import pprint


def data_load(link):
    with open(link, "r") as fp:
        data = json.load(fp)
    return data


# def get_posts():
#     posts = data_load("data/data.json")
#     return posts


def get_posts_with_comments_count():
    posts = data_load("data/data.json")
    comments = data_load("data/comments.json")

    for index, post in enumerate(posts):

        comments_count = 0

        for comment in comments:
            if comment["post_id"] == post["pk"]:
                comments_count += 1

        posts[index]["comments"] = comments_count

    return posts


def get_post_by_pk(post_pk):
    posts = data_load("data/data.json")
    for post in posts:
        if post["pk"] == post_pk:
            return post
    return None


def get_post_comments_by_pk(post_pk):
    comments = data_load("data/comments.json")
    post_comments = []
    for comment in comments:
        if comment["post_id"] == post_pk:
            post_comments.append(comment)
    return post_comments


def search_posts(word):
    posts = data_load("data/data.json")
    comments = data_load("data/comments.json")

    searched_posts = []

    for index, post in enumerate(posts):

        comments_count = 0

        if word.lower() in post["content"].lower():
            searched_posts.append(post)

            for comment in comments:
                if comment["post_id"] == post["pk"]:
                    comments_count += 1

        posts[index]["comments"] = comments_count

    return searched_posts


def get_post_by_name(poster_name):
    posts = get_posts_with_comments_count()
    posts_by_name = []

    for post in posts:
        if poster_name == post["poster_name"]:
            posts_by_name.append(post)

    return posts_by_name