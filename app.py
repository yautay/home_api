from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

relays = []


class Relays(Resource):
    def get(self, name):
        for relay in range(len(relays)):
            print(relay)
            if name == relays[relay]["relay"]:
                return relays[relay]
        return {"relay": None}, 404

    def post(self, name):
        relay = {"relay": name,
                 "time": "546566",
                 "power": False
                 }
        relays.append(relay)
        return relay, 201

    def put(self, name):
        pass


api.add_resource(Relays, "/relay/<string:name>")

app.run()
