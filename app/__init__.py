from flask import Flask
from app.routes import Route

def setup():
    app = Flask(__name__)
    Route(app)
    return app