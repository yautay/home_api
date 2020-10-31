from db import db
from datetime import datetime


class RelayModel(db.Model):
    __tablename__ = "relays"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    state = db.Column(db.String)
    timestamp = db.Column(db.TIMESTAMP)

    localization_id = db.Column(db.Integer, db.ForeignKey("localization.id"))
    localization = db.relationship("LocalizationModel")

    def __init__(self, name, state, localization_id):
        self.name = name
        self.state = state
        self.timestamp = datetime.now()
        self.localization_id = localization_id

    def json(self):
        json = {
            "name": self.name,
            "state": self.state,
            "timestamp": str(self.timestamp)
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
