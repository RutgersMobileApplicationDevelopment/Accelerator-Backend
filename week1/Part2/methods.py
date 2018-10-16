from flask import Flask, request
app = Flask(__name__)

@app.route("/hello", methods=['GET', 'POST'])
def hello():
    return "You sent a " + request.method + " method."

@app.route("/complex", methods=['POST'])
def json_data():
    req_data = request.get_json()
    return req_data['username'] + " who is " + str(req_data['age']) + " likes " + " ".join(req_data['hobbies']) + " and lives in " + req_data['address']['state']
