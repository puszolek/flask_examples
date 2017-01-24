import flask
import os
import json
import codecs
import string
import requests
from flask.ext.api import status
import sys


app = flask.Flask(__name__)
exclude = string.punctuation


#post json to the specified host
def post_json(js, host):
    resp = requests.post(host, json=js, headers={'Content-type':'application/json; charset=UTF-8'})
    return resp.text


@app.route('/', methods=['GET'])
def api_root():
    return 'Welcome'


@app.route('/', methods=['POST'])
def api_response():
    
    #receive json
    js = flask.request.get_json()

    #create json to return
    json_return = {}

    #return string containing json
    return json.dumps(js_return)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)
