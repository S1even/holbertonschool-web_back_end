#!/usr/bin/env python3
"""
Flask application integrating Babel for internationalization (i18n).
Sets up basic configuration for languages, timezone, and locale.
"""
from flask import Flask, render_template
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
# Load configuration from the Config class
app.config.from_object(Config)

# Instantiate Babel in a module-level variable
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the 1-index.html template.
    Returns the HTML string to display the welcome message.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
