from flask_sqlalchemy import SQLAlchemy

import config
from flask import Flask

app = Flask(__name__)

app.config.from_object(config)
db = SQLAlchemy(app)
