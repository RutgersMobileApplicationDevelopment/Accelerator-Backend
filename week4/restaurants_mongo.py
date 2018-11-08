from flask import Flask, request, jsonify
import json
from pymongo import MongoClient
from bson import ObjectId
app = Flask(__name__)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

client = MongoClient('localhost', 27017)

restaurant_db = client['restaurant-db']

restaurants = []
dishes = {}
ratings = {}

@app.route("/restaurants", methods=["POST", "GET"])
def restaurant_list():
    if request.method == 'GET':
        restaurant_coll = restaurant_db['restaurants']
        return JSONEncoder().encode(list(restaurant_coll.find()))
    else:
        # restaurants.append(request.get_json()['restaurant'])
        res = {
            "name": request.get_json()['restaurant'],
            "dishes": [],
            "ratings": []
        }
        restaurant_coll = restaurant_db['restaurants']
        restaurant_coll.insert_one(res)
        return "Done."

@app.route("/restaurants/<res_name>", methods=["DELETE"])
def restaurant_delete(res_name):
    restaurant_coll = restaurant_db['restaurants']
    restaurant_coll.delete_one({"name": res_name})
    return "Done."

@app.route("/restaurants/<res_name>/dishes", methods=["GET", "POST"])
def restaurant_dishes(res_name):
    if request.method == 'GET':
        restaurant_coll = restaurant_db['restaurants']
        return JSONEncoder().encode(restaurant_coll.find_one({"name": res_name})["dishes"])
    else:
        restaurant_coll = restaurant_db['restaurants']
        restaurant_coll.update({"name": res_name}, {"$push": {"dishes": request.get_json()["dish"]}})
        return "Done."

@app.route("/restaurants/<res_name>/ratings", methods=["GET", "POST"])
def restaurant_ratings(res_name):
    if request.method == 'GET':
        restaurant_coll = restaurant_db['restaurants']
        return JSONEncoder().encode(restaurant_coll.find_one({"name": res_name})["ratings"])
    else:
        restaurant_coll = restaurant_db['restaurants']
        restaurant_coll.update({"name": res_name}, {"$push": {"ratings": request.get_json()["rating"]}})
        return "Done."

