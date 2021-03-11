import sys

from flask import Flask
from flask_restful import Api

from resources.root import Root
app = Flask(__name__)
app.secret_key = "secret"
api = Api(app)

api.add_resource(Root, "/")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
