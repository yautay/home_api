import sqlite3
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse


class Relay(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name",
                        type=str,
                        required=True,
                        help="Brief name...")
    parser.add_argument("state",
                        type=bool,
                        required=True,
                        help="This can not be blank!"
                        )
    parser.add_argument("timestamp",
                        type=str,
                        required=True,
                        help="Needs time!")

    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM relays WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        if row:
            return {"relay": {"id": row[0], "name": row[1], "state": row[2], "timestamp": row[3]}}
        else:
            return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x["name"] == name, relays), None):
            return {"message": "An relay with name '{}' already exists.".format(name)}, 400

        data = self.parser.parse_args()
        relay = {"name": name,
                 "time": data["timestamp"],
                 "state": data["power"]
                 }
        relays.append(relay)
        return relay, 201

    @jwt_required()
    def put(self, name):
        relay = next(filter(lambda x: x["name"] == name, relays), None)
        data = self.parser.parse_args()
        if relay is None:
            relay = {"name": name,
                     "time": data["timestamp"],
                     "state": data["power"]
                     }
            relays.append(relay)
        else:
            relay.update(data)
        return relay

    @jwt_required()
    def delete(self, name):
        global relays
        relays = list(filter(lambda x: x["name"] != name, relays))
        return {"message": "Relay deleted"}


class RelayList(Resource):
    def get(self):
        return {"relays": relays}
