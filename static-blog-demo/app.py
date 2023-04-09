from flask import Flask, render_template, jsonify, Request, request
from dataclasses import dataclass, asdict
import uuid
from urllib.parse import urlparse

app = Flask(__name__)

@dataclass
class Post():
    id : int
    title: str
    content: str


lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

example_posts = { 
    0: Post(0, "First post", lorem_ipsum),
    1: Post(1, "Second post", lorem_ipsum),
    2: Post(2, "Third post", lorem_ipsum),
    3: Post(3, "Fourth post", lorem_ipsum),
    4: Post(4, "Fifth post", lorem_ipsum),
    5: Post(5, "Sixth post", lorem_ipsum),
    6: Post(6, "Seventh post", lorem_ipsum),
    7: Post(7, "Eighth post", lorem_ipsum),
    8: Post(8, "Ninth post", lorem_ipsum),
    9: Post(9, "Tenth post", lorem_ipsum),
}

def get_host(req : Request) -> str:
    url = urlparse(req.base_url)
    return url[0] + "://" + url[1]

@app.before_first_request
def setup():
    pass

@app.route("/")
def render_todo():
    host = get_host(request)
    return render_template("index.html", hostname=host, posts=[asdict(post) for post in example_posts.values()])

@app.route("/<int:post_num>", methods=["GET"])
def render_post(post_num : int):
    host = get_host(request)
    post = example_posts.get(post_num)
    if post == None:
        return render_template("show_post.html", hostname=host, post=asdict( Post(0, "404 Not Found", "Post not found.") ))
    return render_template("show_post.html", hostname=host, post=asdict(post))

@app.route("/getinfo", methods=["POST"])
def get_post_info():
    my_json = request.json
    post_num = my_json.get("post_num")
    print(post_num)
    info = {}
    if post_num != None:
        info = asdict(example_posts[post_num])
    return info