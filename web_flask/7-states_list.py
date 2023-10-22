#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, url_for
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    """Setup the application, removing session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """listing all states"""
    states = storage.all(State).values()
    new_list = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=new_list)


if __name__ == '__main__':
    """to prevent from running when imported
    """
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
