from app import db
from app.models.common import BaseDBModel


class Users(db.Model, BaseDBModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), index=True)

    def __init__(self, name):
        self.name = name
