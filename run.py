from flask import Flask
from flask import Response
from taps.dryhop import Dryhop
from taps.corridor import Corridor

app = Flask(__name__)


@app.route("/dryhop")
def dryhop():
    tap = Dryhop()
    data = tap.get_menu().json()
    response = Response(response=data, status=200, mimetype="application/json")
    return response


@app.route("/corridor")
def corridor():
    tap = Corridor()
    data = tap.get_menu().json()
    response = Response(response=data, status=200, mimetype="application/json")
    return response


if __name__ == "__main__":
    app.run()
