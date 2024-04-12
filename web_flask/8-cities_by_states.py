#!/usr/bin/python3
"""This module starts a web application with Flask.

The application listens on 0.0.0.0, port 5000.
Teardown:
    close_session: Remove the current session.
Routes:
    /cities_by_states: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all states and related cities.
    States/cities are sorted by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_session(self):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
