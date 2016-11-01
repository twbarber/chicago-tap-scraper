from flask import Flask
from flask import Response

import dryhop
app = Flask(__name__)


@app.route("/dryhop")
def hello():
    data = dryhop.get_menu().json()
    response = Response(response=data, status=200, mimetype="application/json")
    return response

if __name__ == "__main__":
    app.run()
