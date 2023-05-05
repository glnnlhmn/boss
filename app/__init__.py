from flask import Flask

app = Flask(__name__)

from app.loader import routes
