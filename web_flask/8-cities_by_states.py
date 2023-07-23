#!/usr/bin/python3
""" define a function """


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ Displays a list of States and Cities from DBStorage """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("8-cities_by_states.html", states=sorted_states)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """ remove the current SQLAlchemy Session after each request """
    storage.close()


if __name__ == "__main__":
    """ main function """
    app.run(host="0.0.0.0", port=5000)
