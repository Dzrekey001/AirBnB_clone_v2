#!/usr/bin/python3
"""Importing Flask to run the web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = FLask(__name__)


@app.teardown_appcontext
def teardown(self):
    """restart storage session"""
    storage.close()


@app.route('/states_list', strick_slashes=True)
def state_ls():
    """return the list of states in the storage"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
