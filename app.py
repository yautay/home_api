from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
app.secret_key = "dupa"
api = Api(app)

relays = []


class Relay(Resource):
    def get(self, name):
        relay = next(filter(lambda x: x["relay"] == name, relays), None)
        return {"relay": None}, 200 if relay else 404

    def post(self, name):
        if next(filter(lambda x: x["relay"] == name, relays), None):
            return {"message": "An relay with name '{}' already exists.".format(name)}, 400

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
