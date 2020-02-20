from flask import Flask
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
ma = Marshmallow(app)

from flasktask import routes
