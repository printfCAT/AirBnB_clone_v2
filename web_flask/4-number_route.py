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


@app.route("/python/", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pytext(text):
    """ prints Python followed by respective text or is cool by default """
    text_with_spaces = text.replace("_", " ")
    return("Python {}".format(text_with_spaces))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ prints a number only if its an integer """
    return("{} is a number".format(n))

if __name__ == "__main__":
    """ main function """
    app.run(host='0.0.0.0', port=5000)
