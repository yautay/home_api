from flask_restful import Resource, reqparse


class Root(Resource):
    def get(self):
        return "GET TEST", 200

    def post(self, payload):
        print(payload)
        return "POST TEST", 201

