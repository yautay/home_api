from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from db import db
from security import identity, authenticate
from resources.user import UserRegister
from resources.relay import Relay, RelayList
from resources.localization import Localization, LocalizationList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://rest_api:test1q2w3e@192.168.1.4/kim_home"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "kim.home"
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Relay, "/relay/<string:name>")
api.add_resource(RelayList, "/relays")
api.add_resource(UserRegister, '/register')
api.add_resource(Localization, "/localization/<string:name>")
api.add_resource(LocalizationList, "/localizations")

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=False)
