#!/usr/bin/env python3
"""
Simple Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Class config"""
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCCALE = "en"
    DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def index() -> render_template:
    """Function to render an html page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
