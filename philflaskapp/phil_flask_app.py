"""Example Flask App
"""

from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)


@app.route("/hello", methods=['GET', 'POST'])
def hello_world():
    """Return Hello, World to the caller.
    """
    return "<p>Hello, World!</p>"


@app.route("/", methods=['GET', 'POST'])
def index():
    """The root of the web service.
    """
    return redirect(url_for('hello_world'))


@app.route("/health", methods=['GET'])
def health():
    """Return that the app is healthy. A real health check would actually do
    some sort of check to determine the health. Then if it isn't healthy, it
    would not return any values when GET is requested.
    """
    return '{"health": "healthy"}'
