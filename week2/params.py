from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask"

@app.route("/<word>")
def func(word):
    return word

@app.route("/user/<userid>")
def get_user(userid):
    return "user with userid " + userid

