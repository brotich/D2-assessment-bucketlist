from app import db
from app.models.common import BaseDBModel


class Users(BaseDBModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
