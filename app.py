from flask import Flask, render_template, request
from utils import get_posts, get_post_by_pk, get_post_comments_by_pk

app = Flask(__name__)


@app.route('/',)
def page_index():
    posts = get_posts()
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


app.run(debug=True)
