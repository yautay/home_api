from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

relayDB = [
    {
        "name": "dzbaneczniki",
        "properties": {
                "timestamp": "2020-12-12 23:21",
                "power": True
        }
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/relay/<string:name>", methods=["POST"])
def create_relay(name):
    request_data = request.get_json()
    new_relay = {
        "name": name,
        "properties": {
            "timestamp": request_data["timestamp"],
            "power": request_data["power"]
        }
    }
    relayDB.append(new_relay)
    return jsonify(relayDB)


@app.route("/relay")
def get_relays():
    return jsonify({"relays": relayDB})


@app.route("/relay/<string:name>")
def get_relay(name):
    for relay in range(len(relayDB)):
        if relayDB[relay]["name"] == name:
            return jsonify(relayDB[relay])
    else:
        return "Not found"


@app.route("/relay/<string:name>/<string:item>")
def get_relay_item(name, item):
    for relay in range(len(relayDB)):
        if relayDB[relay]["name"] == name:
            if item == "power":
                return jsonify(relayDB[relay]["properties"]["power"])
            elif item == "timestamp":
                return jsonify(relayDB[relay]["properties"]["timestamp"])
            else:
                return "Not found!!!!"
    else:
        return "Not found!!!!"


if __name__ == '__main__':
    app.run()
