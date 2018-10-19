from flask import Flask, request
app = Flask(__name__)

users = []

@app.route("/users", methods=["POST", "GET"])
def restaurant_list():
    if request.method == 'GET':
        return ", ".join(users)
    else:
        users.append(request.get_json()['user'])
        return "Done."

@app.route("/user/<username>", methods=["DELETE", "PUT"])
def get_user(username):
    if request.method == "DELETE":
        users.remove(username)
        return "Deleted user with username " + username
    else:
        users.remove(username)
        users.append(request.get_json()['user'])
        return "Replaced " + username + " with " + request.get_json()['user']

