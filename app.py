from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required

from security import identity, authenticate

app = Flask(__name__)
app.secret_key = "dupa"
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

relays = []


class Relay(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("power",
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
        relay = next(filter(lambda x: x["relay"] == name, relays), None)
        return {"relay": relay}, 200 if relay else 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x["relay"] == name, relays), None):
            return {"message": "An relay with name '{}' already exists.".format(name)}, 400

        data = self.parser.parse_args()
        relay = {"relay": name,
                 "time": data["timestamp"],
                 "power": data["power"]
                 }
        relays.append(relay)
        return relay, 201

    @jwt_required()
    def put(self, name):
        relay = next(filter(lambda x: x["relay"] == name, relays), None)
        data = self.parser.parse_args()
        if relay is None:
            relay = {"relay": name,
                     "time": data["timestamp"],
                     "power": data["power"]
                     }
            relays.append(relay)
        else:
            relay.update(data)
        return relay

    @jwt_required()
    def delete(self, name):
        global relays
        relays = list(filter(lambda x: x["relay"] != name, relays))
        return {"message": "Relay deleted"}


api.add_resource(Relay, "/relay/<string:name>")


class RelayList(Resource):
    def get(self):
        return {"relays": relays}


api.add_resource(RelayList, "/relays")


app.run(port=5000, debug=False)
