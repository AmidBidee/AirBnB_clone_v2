#!/usr/bin/python3
"""
AirBnB Clone
Flask config file
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states')
def states():
    """retrieve all states"""
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_given_id(id):
    """retrieve a state"""
    states = storage.all("State")
    found_state = ""
    for s_id in states:
        if s_id == id:
            found_state = states[s_id]

    return render_template('9-states.html',
                           state=found_state)


@app.teardown_appcontext
def teardown(err):
    """close all active db session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
