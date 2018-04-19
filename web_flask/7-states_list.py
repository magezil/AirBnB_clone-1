#!/usr/bin/python3
"""
    Start Flask web application with HBNB data
    Route /states_list displays HTML page with States listed alphabetically
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
        Route /states_list displays HTML page with States listed alphabetically
    """
    states = storage.all(cls=State)
    return render_template('7-states_list.html', states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
