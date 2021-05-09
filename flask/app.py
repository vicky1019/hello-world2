# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief: a simple instance about how to create a http api interface with python

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return jsonify({"msg": "you are brilliant!"})

# start server
app.run(host="0.0.0.0", port=8000, debug=True)
