from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.extension import db
from app.util import as_dictionary


class UsersEntity(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    email = Column(String(255), unique=True)

    def __init__(self, name=None, email=None, nick=None):
        self.name = name
        self.email = email
        self.nick = nick

    def __repr__(self):
        return '<User %r>' % self.name

    def as_dict(self):
        return as_dictionary(self)
