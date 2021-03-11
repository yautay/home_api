from flask import request
from flask_restful import Resource


class Root(Resource):
    def get(self):
        data = request.headers.environ
        for key in data:
            print("{} -> {}".format(key, data[key]))
        payload = request.data
        print(payload)
        return data["QUERY_STRING"], 200

    def post(self):
        data = request.headers.environ
        for key in data:
            print("{} -> {}".format(key, data[key]))
        payload = request.data
        print(payload)
        return "OK", 200

