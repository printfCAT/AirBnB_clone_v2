#!/usr/bin/python3
""" define a function """


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Displays a list of all State objects in DBStorage sorted by name """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ remove the current SQLAlchemy Session after each request """
    storage.close()


if __name__ == "__main__":
    """ main function """
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
