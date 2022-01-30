from flask import Flask, render_template, request
from utils import get_posts_with_comments_count, get_post_by_pk, \
    get_post_comments_by_pk, search_posts

app = Flask(__name__)


@app.route('/',)
def page_index():
    posts = get_posts_with_comments_count()
    return render_template("index.html", posts=posts)


@app.route('/posts/<int:post_pk>',)
def page_post(post_pk):
    post = get_post_by_pk(post_pk)
    comments = get_post_comments_by_pk(post_pk)
    comments_count = len(comments)
    return render_template("post.html",
                           post=post,
                           comments=comments,
                           comments_count=comments_count
                           )


@app.route('/search',)
def page_search():
    word = request.args['s']

    posts = search_posts(word)
    posts_count = len(posts)

    return render_template("search.html", word=word, posts=posts, posts_count=posts_count)


app.run(debug=True)
