#!/usr/bin/python3
""" Starts a Flash Web Application """
import uuid
from flask import Flask, render_template, url_for
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    """Setup the application, removing session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def list_states():
    """listing all states"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def list_states_id(id):
    """/states/<id> all states"""
    selected_state = None
    for state in storage.all(State).values():
        if state.id == id:
            selected_state = state
    if selected_state is not None:
        cities = sorted(selected_state.cities, key=lambda city: city.name)
    return render_template('9-states.html', state=selected_state, cities=cities)


if __name__ == '__main__':
    """to prevent from running when imported
    """
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
