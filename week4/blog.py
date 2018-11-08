from flask import Flask, request, jsonify
import json
from pymongo import MongoClient
from bson import ObjectId
import datetime
app = Flask(__name__)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

client = MongoClient('localhost', 27017)

blog_db = client['blog-db']

@app.route("/users", methods=["POST", "GET"])
def users():
    if request.method == 'GET':
        users = blog_db['users']
        return JSONEncoder().encode(list(users.find()))
    else:
        body = request.get_json()
        users = blog_db["users"]
        user = {
            "username": body["username"],
            "name": body["name"],
            "password": body["password"],
            "created": str(datetime.datetime.now())
        }
        users.insert_one(user)
        return "Done."