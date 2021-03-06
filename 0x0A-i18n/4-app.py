#!/usr/bin/env python3
""" basic Flask app """

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET method """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ Get locale from request """
    if request.args.get('locale'):
        return request.args.get('locale')
    return request.accept_languages.best_match(Config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
