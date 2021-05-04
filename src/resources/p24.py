from flask_restful import Resource


class P24(Resource):
    def __init__(self, p24_response=True):
        self.resp = p24_response
        if self.resp:
            response_json = {
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
        else:
            response_json = {
                "data": [],
                "responseCode": 0
            }

    def get(self):
        if self.resp:
            return self.response_json, 200
        else:
            return self.response_json, 202

    def post(self):
        if self.resp:
            return self.response_json, 200
        else:
            return self.response_json, 202
