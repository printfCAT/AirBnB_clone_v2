#!/usr/bin/python3
""" define a function """


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ prints Hello HBNB! """
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ prints HBNB """
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """ prints C followed by respective text """
    text_with_spaces = text.replace("_", " ")
    return("C {}".format(text_with_spaces))


if __name__ == "__main__":
    """ main function """
    app.run(host='0.0.0.0', port=5000)
