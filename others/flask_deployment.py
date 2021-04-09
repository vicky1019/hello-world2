# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief:

from flask import Flask, render_template


# app = Flask(__name__)   # name the flask as app
application = Flask(__name__)



@application.route('/')
def index():
    return "<h1 style='color:blue'>Hello Flask!</h1>"


# @app.route('/test', methods=['GET', 'POST'])
@application.route('/test', methods=['POST'])
def test():
    # success or not
    return 'success'


if __name__ == "__main__":
    # app.run(debug=True, port=5000)
    application.run(debug=True, host='0.0.0.0')