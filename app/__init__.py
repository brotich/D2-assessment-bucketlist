from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)

app.config.from_object(config)
db = SQLAlchemy(app)

from app.api.sample import sample_mod
from app.api.users import users_bp

app.register_blueprint(sample_mod)
app.register_blueprint(users_bp)
