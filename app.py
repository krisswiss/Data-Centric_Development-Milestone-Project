import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    shoes = mongo.db.shoes.find()
    return render_template("home.html", shoes=shoes)


@app.route('/all_shoes')
def all_shoes():
    shoes = mongo.db.shoes.find()
    return render_template("shoes.html", shoes=shoes)


@app.route('/road_shoes')
def road_shoes():
    shoes = mongo.db.shoes.find({"cycling_type": "road"})
    return render_template("shoes.html", shoes=shoes)


@app.route('/mtb_shoes')
def mtb_shoes():
    shoes = mongo.db.shoes.find({"cycling_type": "mtb"})
    return render_template("shoes.html", shoes=shoes)


@app.route('/shoe/<shoe_id>')
def shoe(shoe_id):
    shoe = mongo.db.shoes.find({"_id": ObjectId(shoe_id)})
    reviews = mongo.db.reviews.find({"shoe_id": ObjectId(shoe_id)})
    return render_template("shoe.html", shoe=shoe, reviews=reviews)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)