from flask_restful import Resource


class P24pass(Resource):
    def __init__(self):
        self.response_json = {
            "data": {
                "name": "JAN NOWAK",
                "street": "UL.TĘCZOWA 15",
                "city": "POZNAŃ",
                "postCode": "60-275",
                "iban": "49658765504459786094965876",
                "originalString": "JAN NOWAK UL.TĘCZOWA 15 60-275 POZNAŃ"
            },
            "responseCode": "0"
        }

    def get(self):
        return self.response_json, 200

    def post(self):
        return self.response_json, 200
