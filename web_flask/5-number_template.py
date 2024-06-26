#!/usr/bin/python3
""" This module defines few apps with Flask

    Listen on 0.0.0.0, port 5000.
    Routes:
        /: Displays "Hello HBNB!".
        /hbnb: Displays "HBNB".
        /c/<text>: Displays "C" followed by the values of <text>.
        /python/<text>: Displays "Python" followed by <text> or "is cool".
        /number/<n>: Displays "<n> is a number" only if "n" is an integer.
        /number_template/<n>: Display a HTML page only if "n" is an integer.
"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays "<n> is a number" only if "n" is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if "n" is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
