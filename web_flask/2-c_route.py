#!/usr/bin/python3
""" This module defines few apps with Flask"""
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
    """C page"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
