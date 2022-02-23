#!/usr/bin/python3
"""Flask app config"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    """say hello"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """simply return hbnb"""
    return "HBNB"


@app.route('/c/<string:s>')
def c(s):
    """
    replace '_' in string with space
    """
    new_s = s.replace("_", " ")
    return "C {}".format(new_s)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
