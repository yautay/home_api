from flask import Flask
from flask_restful import Api
from resources.p24 import P24

app = Flask(__name__)
app.secret_key = "1q2w3e"
api = Api(app)

end200 = P24
end202 = P24(p24_response=False)

api.add_resource(end200, "/p24mock/true")
api.add_resource(end202, "/p24mock/false")

if __name__ == '__main__':
    app.run(port=5000, debug=False)
