#!/usr/bin/python3
"""
    A script that starts a Flask web application:

    The web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text
        variable (replace underscore _ symbols with a space )
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Returns Hello HBNB"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Return a formated text"""
    txt = text.replace("_", " ")
    return ("C {}".format(txt))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)
