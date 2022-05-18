#!/usr/bin/env python3
"""
Simple Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Class config"""
    LANGUAGES = ["en", "fr"]
    default_locale = "en"
    default_timezone = "UTC"


config = Config()


app = Flask(__name__)
app.config.from_object(config)
babel = Babel(
              app=app,
              default_locale=config.default_locale,
              default_timezone=config.default_timezone
              )


@app.route("/")
def index() -> render_template:
    """Function to render an html page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
