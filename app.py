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


@app.route('/add_shoe')
def add_shoe():
    return render_template('addshoe.html')


@app.route('/insert_shoe', methods=['POST'])
def insert_shoe():
    tasks =  mongo.db.shoes
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('all_shoes'))


@app.route('/edit_shoe/<shoe_id>')
def edit_shoe(shoe_id):
    shoe = mongo.db.shoes.find({"_id": ObjectId(shoe_id)})
    return render_template('editshoe.html', shoe=shoe)


@app.route('/update_shoe/<shoe_id>', methods=["POST"])
def update_shoe(shoe_id):
    shoe = mongo.db.shoes
    shoe.update( {'_id': ObjectId(shoe_id)},
    {
        'brand': request.form.get('brand'),
        'model': request.form.get('model'),
        'cycling_type': request.form.get('cycling_type'),
        'gender': request.form.get('gender'),
        'closure': request.form.get('closure'),
        'sole': request.form.get('sole'),
        'picture_url': request.form.get('picture_url'),
        'description': request.form.get('description')
    })
    return redirect(url_for('all_shoes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)