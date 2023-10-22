#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, url_for
from models import storage
from models.state import State
from models.city import City
from os import getenv
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    """Setup the application, removing session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_states():
    """listing all states"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    cities = {}
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        for state in states:
            cities[state.id] = sorted(state.cities, key=lambda city: city.name)
    elif getenv('HBNB_TYPE_STORAGE') == 'file':
        for state in states:
            cities[state.id] = sorted(state.cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


if __name__ == '__main__':
    """to prevent from running when imported
    """
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
