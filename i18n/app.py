#!/usr/bin/env python3
"""
Flask application integrating Babel for internationalization (i18n).
Determines user locale and timezone, and displays the localized current time.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
from typing import Union, Dict
from datetime import datetime


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
    """
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    header_locale = request.accept_languages.best_match(
        app.config['LANGUAGES']
    )
    if header_locale:
        return header_locale

    return app.config['BABEL_DEFAULT_LOCALE']


def get_timezone() -> str:
    """
    Determines the appropriate timezone.
    Validates timezone using pytz.
    """
    tz = request.args.get('timezone')
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        tz = g.user.get('timezone')
        try:
            pytz.timezone(tz)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone
)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the index.html template.
    Generates the current time formatted according to the user's
    locale and timezone.
    """
    current_time = format_datetime(datetime.utcnow())
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
