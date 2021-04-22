#!/usr/bin/env python3
""" basic Flask app """

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'


class Config:
    """Config class
    """
    LANGUAGES = ['en', 'fr']


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET method """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
