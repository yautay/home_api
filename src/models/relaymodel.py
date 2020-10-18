import sqlite3
from db import db


class RelayModel(db.Model):
    __tablename__ = "relays"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    state = db.Column(db.String)
    timestamp = db.Column(db.String)

    def __init__(self, _id, name, state, timestamp):
        self.id = _id
        self.name = name
        self.state = state
        self.timestamp = timestamp

    def json(self):
        json = {
            "id": self.id,
            "name": self.name,
            "state": self.state,
            "timestamp": self.timestamp
        }
        return json

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
