#!/usr/bin/python3
""" define a function """


from flask import Flask, render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def index(n):
    """ returns a HTML if n is an integer """
    title = "HBNB"
    H1 = n
    return render_template("5-number.html", title=title, H1=H1)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def oddeven(n):
    """ returns even|odd if n is even|odd """
    title = "HBNB"
    H1 = n
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", title=title, H1=H1, evenodd="even")
    else:
        return render_template("6-number_odd_or_even.html", title=title, H1=H1, evenodd="odd")


if __name__ == "__main__":
    """ main function """
    app.run(host='0.0.0.0', port=5000)
