#!/usr/bin/env python3
"""
Simple Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Class config"""
    LANGUAGES = ["en", "fr"]


config = Config()


app = Flask(__name__)
app.config.from_object(config)
babel = Babel(app)


@app.route("/")
def index():
    """Function to render an html page"""
    return render_template('0-index.html')


@babel.localeselector
def get_locale():
    """Get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Get Timezone"""
    return "UTC"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
