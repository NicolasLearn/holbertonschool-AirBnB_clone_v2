#!/usr/bin/python3
""" This module defines few apps with Flask

    Listen on 0.0.0.0, port 5000.
    Routes:
        /: Displays "Hello HBNB!"
        /hbnb: Displays "HBNB"
        /c/<text>: Displays "C" followed by the values of <text>.
        /python/<text>: Displays "Python" followed by <text> or "is cool".
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """home page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """HBNB page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    """Displays 'C' followed by the value of <text>.
    Replaces underscores with space.
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
def Python_text(text):
    """Displays 'Python' followed by the value of <text>.
    Replaces underscores with space.
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
