from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import identity, authenticate
from user import UserRegister
from relay import Relay, RelayList

app = Flask(__name__)
app.secret_key = "kim.home"
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Relay, "/relay/<string:name>")
api.add_resource(RelayList, "/relays")
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=False)
