#!/usr/bin/env python3
"""
Flask application integrating Babel for internationalization (i18n).
Mocks a user login system and stores user data in flask.g.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config:
    """
    Configuration class for the Flask application.
    Defines available languages and sets Babel default locale and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Retrieves a user dictionary based on the user ID passed in the
    'login_as' URL parameter.
    Returns None if the ID is not found or not passed.
    """
    login_id = request.args.get('login_as')
    if login_id:
        try:
            return users.get(int(login_id))
        except ValueError:
            return None
    return None


@app.before_request
def before_request() -> None:
    """
    Executed before all other functions.
    Finds a user and sets it as a global on flask.g.user.
    """
    g.user = get_user()


def get_locale() -> str:
    """
    Determines the best match with our supported languages.
    Checks for a 'locale' parameter in the URL request first.
    If not, it falls back to the Accept-Language header.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the 5-index.html template.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
