import sqlite3
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse


class Relay(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("state",
                        type=bool,
                        required=True,
                        help="This can not be blank!"
                        )
    parser.add_argument("timestamp",
                        type=str,
                        required=True,
                        help="Needs time!")

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM relays WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        if row:
            return {"relay": {"id": row[0], "name": row[1], "state": row[2], "timestamp": row[3]}}

    @classmethod
    def insert(cls, relay):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO relays VALUES (NULL , ?, ?, ?)"
        cursor.execute(query, (relay["name"], relay["state"], relay["timestamp"],))
        connection.commit()
        connection.close()

    @classmethod
    def update(cls, relay):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE relays SET state=?, timestamp=? WHERE name=?"
        cursor.execute(query, (relay["state"], relay["timestamp"], relay["name"]))
        connection.commit()
        connection.close()

    @jwt_required()
    def get(self, name):
        try:
            relay = self.find_by_name(name)
        except:
            return {"message": "An error occurred searching for item"}, 500
        if relay:
            return relay
        else:
            return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name):
        try:
            if self.find_by_name(name):
                return {"message": "An relay with name '{}' already exists.".format(name)}, 400
        except:
            return {"message": "An error occurred searching for item"}, 500

        data = self.parser.parse_args()
        relay = {"name": name,
                 "state": data["state"],
                 "timestamp": data["timestamp"]
                 }
        try:
            self.insert(relay)
        except:
            return {"message": "An error occurred inserting the item"}, 500

        return relay, 201

    @jwt_required()
    def put(self, name):
        data = self.parser.parse_args()
        updated_relay = {"name": name,
                 "state": data["state"],
                 "timestamp": data["timestamp"]
                 }
        try:
            relay = self.find_by_name(name)
        except:
            return {"message": "An error occurred searching for item"}, 500

        if relay is None:
            try:
                self.insert(updated_relay)
            except:
                return {"message": "An error occurred inserting the item"}, 500
        else:
            try:
                self.update(updated_relay)
            except:
                return {"message": "An error occurred updating the item"}, 500

        return updated_relay

    @jwt_required()
    def delete(self, name):
        try:
            if not self.find_by_name(name):
                return {"message": "An relay with name '{}' does not exists.".format(name)}, 404
        except:
            return {"message": "An error occurred searching for item"}, 500

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM relays WHERE name =?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {"message": "Relay deleted"}


class RelayList(Resource):
    def get(self):
        return {"relays": relays}
