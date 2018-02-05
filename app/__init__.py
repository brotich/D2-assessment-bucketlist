from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)

app.config.from_object(config)
db = SQLAlchemy(app)

from app.api.sample import sample_mod

app.register_blueprint(sample_mod)
