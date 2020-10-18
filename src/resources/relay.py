import sqlite3
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.relaymodel import RelayModel


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

    @jwt_required()
    def get(self, name):
        try:
            print("ddd")
            relay = RelayModel.find_by_name(name)
        except:
            return {"message": "An error occurred searching for item"}, 500
        if relay:
            return relay.json()
        else:
            return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name):
        try:
            if RelayModel.find_by_name(name):
                return {"message": "An relay with name '{}' already exists.".format(name)}, 400
        except:
            return {"message": "An error occurred searching for item"}, 500

        data = self.parser.parse_args()
        relay = RelayModel(_id=None, name=name, state=data["state"], timestamp=data["timestamp"])
        try:
            relay.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}, 500

        return relay.json(), 201

    @jwt_required()
    def put(self, name):
        data = self.parser.parse_args()

        try:
            relay = RelayModel.find_by_name(name)
        except:
            return {"message": "An error occurred searching for item"}, 500

        if relay is None:
            relay = RelayModel(_id=None, name=name, state=data["state"], timestamp=data["timestamp"])
        else:
            relay.state = data["state"]
            relay.timestamp = data["timestamp"]

        try:
            relay.save_to_db()
        except:
            return {"message": "An error occurred updating the item"}, 500

        return relay.json()

    @jwt_required()
    def delete(self, name):
        try:
            relay = RelayModel.find_by_name(name)
        except:
            return {"message": "An error occurred searching for item"}, 500
        if relay is not None:
            try:
                relay.delete_from_db()
                return {"message": "Relay deleted"}
            except:
                return {"message": "An error occurred deleting item"}, 500
        else:
            return {"message": "An relay with name '{}' does not exists.".format(name)}, 404



class RelayList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM relays"
        result = cursor.execute(query)
        relays = []
        for row in result:
            relays.append({"id": row[0], "name": row[1], "state": row[2], "timestamp": row[3]})
        connection.commit()
        connection.close()
        return relays

