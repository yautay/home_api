from flask import Flask
from flask_restful import Api
from resources.p24pass import P24pass
from resources.p24wait import P24wait

app = Flask(__name__)
app.secret_key = "1q2w3e"
api = Api(app)

api.add_resource(P24pass, "/p24mock/true")
api.add_resource(P24wait, "/p24mock/false")

if __name__ == '__main__':
    app.run(port=5000, debug=False)
