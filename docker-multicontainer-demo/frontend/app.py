from urllib.parse import urlparse
from flask import Flask, render_template, request, jsonify
import os
import requests

def load_env(names):
    env_dict = { "unset": [] }
    for nm in names:
        env = os.environ.get(nm)
        
        if env == None:
            env_dict['unset'].append(nm)
            continue

        env_dict[nm] = env
    return env_dict

app = Flask(__name__)
env = load_env(["WRITER_ENDPOINT"])

if len(env["unset"]) > 0:
    print ("Exit due to env variables being unset.")
    exit(0)

@app.route("/", methods=["GET"])
def show_content():
    url = urlparse(request.base_url)
    host = url[0] + "://" + url[1]
    return render_template("index.html", endpoint=host)

@app.route("/submit", methods=["POST"])
def send_json():
    writer_endpoint = env["WRITER_ENDPOINT"]
    res = requests.post(writer_endpoint, json=request.json)
    print (res.json())
    return jsonify(res.json())