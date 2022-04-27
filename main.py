from flask import Flask, request
import requests
import json


app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    return "Hello World"

@app.route('/check-status')
def check_status():
    # if key doesn't exist, returns None
    url = request.args.get('url')
    response = requests.get(url, verify=False, allow_redirects=False)
    response_time = round((response.elapsed.total_seconds() * 1000), 1)
    data = {
        'url': url,
        'status-code': response.status_code,
        'response-time': response_time,
    }
    return json.dumps(data)