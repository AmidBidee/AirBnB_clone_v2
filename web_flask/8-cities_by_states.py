#!/usr/bin/python3
"""
AirBnB Clone
Flask config file
"""
from flask import Flask, abort, render_template
from models import *
from models import storage

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:s>')
def python(s="is cool"):
    """more replaces"""
    new_s = s.replace("_", " ")
    return "Python {}".format(new_s)


@app.route('/number/<n>')
def number(n):
    """check if number"""
    try:
        n = int(n)
        return "{} is a number".format(n)
    except Exception:
        abort(404)


@app.route('/number_template/<int:n>')
def number_template(n):
    """render a template"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """render more template"""
    return render_template('6-number_odd_or_even.html', num=n)


@app.route('/states_list')
def states_list():
    """retrieves all states"""
    return render_template('7-states_list.html',
                           states=storage.all("State"))


@app.route('/cities_by_states')
def cities_by_states():
    """retrieve all cities by states"""
    return render_template('8-cities_by_states.html',
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown(err):
    """remove all active db sessions"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
