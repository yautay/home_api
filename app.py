from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

relays = []


class Relay(Resource):
    def get(self, name):
        for relay in range(len(relays)):
            print(relay)
            if name == relays[relay]["relay"]:
                return relays[relay]
        return {"relay": None}, 404

    def post(self, name):
        data = request.get_json()
        relay = {"relay": name,
                 "time": data["timestamp"],
                 "power": data["power"]
                 }
        relays.append(relay)
        return relay, 201

    def put(self, name):
        pass


api.add_resource(Relay, "/relay/<string:name>")


class RelayList(Resource):
    def get(self):
        return {"relays": relays}


api.add_resource(RelayList, "/relays")


app.run(port=5000, debug=True)
