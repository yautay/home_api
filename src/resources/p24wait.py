from flask_restful import Resource


class P24wait(Resource):
    def __init__(self):
        self.response_json = {
            "data": [],
            "responseCode": 0
        }

    def get(self):
        return self.response_json, 202

    def post(self):
        return self.response_json, 202
