from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from db import db
from security import identity, authenticate
from resources.user import UserRegister
from resources.relay import Relay, RelayList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "kim.home"
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Relay, "/relay/<string:name>")
api.add_resource(RelayList, "/relays")
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=False)
