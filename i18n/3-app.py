#!/usr/bin/env python3
"""
Flask application integrating Babel for internationalization (i18n).
Parametrizes templates to allow dynamic translations.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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


def get_locale() -> str:
    """
    Determines the best match with our supported languages based on
    the Accept-Language header from the client's request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the 3-index.html template.
    Returns the HTML string to display the translated welcome message.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
