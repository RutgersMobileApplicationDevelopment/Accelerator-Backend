from flask import Flask, request, jsonify, Response
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
        return Response(JSONEncoder().encode(list(users.find())), mimetype='application/json')
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

@app.route("/posts", methods=["POST", "GET"])
def posts():
    if request.method == 'POST':
        body = request.get_json()
        post = {
            "title": body["title"],
            "body": body["body"],
            "userid": body["userid"],
            "name": body["name"],
            "created": str(datetime.datetime.now()),
            "comments": []
        }
        posts = blog_db["posts"]
        posts.insert_one(post)
        return "Done."
    else:
        posts = blog_db["posts"]
        return Response(JSONEncoder().encode(list(posts.find())), mimetype='application/json')

@app.route("/posts/<postid>", methods=["DELETE", "GET"])
def single_post(postid):
    if request.method == 'GET':
        posts = blog_db["posts"]
        return Response(JSONEncoder().encode(posts.find_one({"_id": ObjectId(postid)})), mimetype='application/json')
    else:
        posts = blog_db["posts"]
        posts.delete_one({"_id": ObjectId(postid)})
        return "Done."

@app.route("/posts/<postid>/comments", methods=["POST", "GET"])
def comments(postid):
    if request.method == 'GET':
        return Response(JSONEncoder().encode(posts.find_one({"_id": ObjectId(postid)})["comments"]), mimetype='application/json')
    else:
        body = request.get_json()
        new_comment = {
            "body": body["body"],
            "userid": body["userid"],
            "name": body["name"]
        }
        posts = blog_db["posts"]
        posts.update_one({"_id": ObjectId(postid)}, {"$push": {"comments": new_comment}})
        return "Done."
