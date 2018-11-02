from flask import Flask, request
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('localhost', 27017)

restaurant_db = client['restaurant-db']

restaurants = []
dishes = {}
ratings = {}

@app.route("/restaurants", methods=["POST", "GET"])
def restaurant_list():
    if request.method == 'GET':
        return ", ".join(restaurants)
    else:
        # restaurants.append(request.get_json()['restaurant'])
        res = {
            "name": request.get_json()['restaurant']
        }
        restaurant_coll = restaurant_db['restaurants']
        restaurant_coll.insert_one(res)
        return "Done."

@app.route("/restaurants/<res_name>", methods=["DELETE"])
def restaurant_delete(res_name):
    if (dishes.get(res_name, None) == None):
        dishes[res_name] = []
    if (ratings.get(res_name, None) == None):
        ratings[res_name] = []
    restaurants.remove(res_name)
    del dishes[res_name]
    del ratings[res_name]
    return "Done."

@app.route("/restaurants/<res_name>/dishes", methods=["GET", "POST"])
def restaurant_dishes(res_name):
    if (dishes.get(res_name, None) == None):
        dishes[res_name] = []
    if request.method == 'GET':
        return ", ".join(dishes[res_name])
    else:
        dishes[res_name].append(request.get_json()['dish'])
        return "Done."

@app.route("/restaurants/<res_name>/ratings", methods=["GET", "POST"])
def restaurant_ratings(res_name):
    if (ratings.get(res_name, None) == None):
        ratings[res_name] = []
    if request.method == 'GET':
        return ", ".join(ratings[res_name])
    else:
        ratings[res_name].append(request.get_json()['dish'])
        return "Done."

