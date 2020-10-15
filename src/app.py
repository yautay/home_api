from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required

from src.security import identity, authenticate
from src.user import UserRegister

app = Flask(__name__)
app.secret_key = "kim.home"
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

relays = []


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
        relay = next(filter(lambda x: x["name"] == name, relays), None)
        return {"relay": relay}, 200 if relay else 404

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


api.add_resource(Relay, "/relay/<string:name>")
api.add_resource(RelayList, "/relays")
api.add_resource(UserRegister, '/register')


app.run(port=5000, debug=False)
