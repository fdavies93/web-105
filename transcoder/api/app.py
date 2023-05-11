from flask import Flask, flash, request, redirect, send_from_directory, make_response, jsonify
from os import listdir, environ
from os.path import isfile, join
import time
import json
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)

def _build_cors_preflight_response():
    response = make_response()
    print("building CORS")
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def load_env(names):
    env_dict = { "unset": [] }
    for nm in names:
        env = environ.get(nm)
        
        if env == None:
            env_dict['unset'].append(nm)
            continue

        env_dict[nm] = env
    return env_dict

env = load_env(["FILE_PATH"])

for required in ["FILE_PATH"]:
    if required not in env:
        print("A required env variable was not found. Exiting process.")
        exit(0)

path = env["FILE_PATH"]

ALLOWED_EXTENSIONS = ["mp4", "mov"]

def get_extension(filename : str):
    return filename.rsplit('.', 1)[1].lower()

def is_allowed(filename : str):
    return '.' in filename and get_extension(filename) in ALLOWED_EXTENSIONS

@app.route("/<path:filename>", methods=["GET"])
def download_file(filename):
    return send_from_directory(env["FILE_PATH"],filename)

@app.route("/", methods=["GET"])
def get_files():
    print("GET route")
    files = [f for f in listdir(env["FILE_PATH"]) if isfile(join(env["FILE_PATH"], f))]
    return {"files": files}

@app.before_request
def handle_options():
    if request.method == "OPTIONS":
        print("Call to OPTIONS")
        return _build_cors_preflight_response()

@app.route("/", methods=["POST"])
def upload_file():
    print(request.files)
    if 'file' not in request.files:
        print("Couldn't find local file.")
        return redirect(request.url)
    file = request.files['file']
    print(file.filename)
    if file.filename == '':
        print ("File has no name.")
        return redirect(request.url)
    if file and is_allowed(file.filename):
        filename = secure_filename(file.filename)
        print(f"Saving file {filename}")
        unique_id = str(uuid.uuid4())
        filename = f"{unique_id}.{get_extension(filename)}"
        file.save(join(env["FILE_PATH"], filename))
        res = jsonify( {"id": unique_id, "file": filename} )
        _corsify_actual_response(res)
        return res
    return ''