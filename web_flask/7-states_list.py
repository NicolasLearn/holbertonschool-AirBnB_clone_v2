#!/usr/bin/python3
"""This module starts a web application with Flask.

The application listens on 0.0.0.0, port 5000.
Teardown:
    close_session: Remove the current session.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all States sorted by name."""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(self):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
