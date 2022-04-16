from flask import *
app = Flask(__name__)


@app.route("/") #URLと紐付け
def main():
    return "helloworld"


@app.route("/<name>")
def hello_name(name):
    return "Hello{}".format(name)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)