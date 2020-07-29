from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

relayDB = [
    {
        "name": "dzbaneczniki",
        "properties": {
                "timestamp": "2020-12-12 23:21",
                "power": True
        }
    }
]


class Relay(Resource):
    def get(self, name):
        return {"relay": name}


api.add_resource(Relay, "/relay/<string:name>")


app.run()
