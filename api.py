import json
import logging
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
#Assignment 4
@app.route("/")
def hello_world():
    app.logger.info('Welcomee And Hello')
    
    return jsonify(
        username="daniel",
        email="daniel@godpeem.com",
        id="123",
    )

@app.route("/food",methods=['GET'])
def display_data():
    app.logger.info("Requesting food data")
    jsonbody = {
        "food" : [],
    }
    with open('food_data.txt', 'r') as f:
        data = f.read()
        data = data.split('\n')
        for item in data:
            jsonbody["food"].append(item)
        return jsonify(jsonbody)


@app.route("/save/<foodname>")
def save(foodname):
    app.logger.info("Saving food data")
    with open('food_data.txt', 'a') as f:
        f.write('\n'+foodname)
        f.close()
    jsonbody = {
        "food" : foodname,
    }
    return jsonify(jsonbody)
#Assignment 5
@app.after_request
def logging_response_code(response):
    status_tostring = response.status
    logging.warning("Status: %s" % status_tostring)
    return response
