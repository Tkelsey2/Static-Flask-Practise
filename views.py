#Setting up routes
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

#request allows us to do profile?name= in browser

#initialise Blueprint
views = Blueprint(__name__, "views")

#creating / route
@views.route("/")
def home():
    #allows for passing of html to Python, can also pass variables INTO the html
    return render_template("index.html", name="Tyler")

@views.route("/profile")
def profile():
    #we can use request.args as dictionary to access query parameters
    args = request.args
    #allows to get access to query parameter if it exists
    name = args.get('name')
    return render_template("index.html", name=name)

#returning/sending JSON
@views.route("/json")
def get_json():
    #now we return a python dictionary (jsonify)
    return jsonify({'name': 'Tyler', 'email' : 'tkelsey2@hotmail.com', 'password': 'TylerIsSickAtPython'})

#get data from incoming request (accessing JSON from a route)
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

#redirecting
@views.route("/go-to-json")
def go_to_json():
    return redirect(url_for("views.get_json"))


