#!/usr/bin/env python3
"""
Basic Flask application setting up a simple index route.
This module initializes the Flask app and renders a basic HTML template.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the basic 0-index.html template.
    Returns the rendered HTML string to the client.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
