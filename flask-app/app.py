# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief: a simple instance about how to create a http api interface with python


from flask import Flask
from flask import jsonify

app = Flask(__name__)

# two ways of your requests(methods=)
# 1.get
# 2.post
# the different between "GET" and "POST"
# "GET": you can see the parameters in the URL,and the max is 1024 byte
# "POST": no byte limited, and date transfer by forms,usually file uploads and content includes passwords etc.
@app.route("/", methods=["GET"])
def hello():
    return jsonify({"msg": "you are brilliant!"})



# start server
app.run(host="0.0.0.0", port=8000, debug=True)
