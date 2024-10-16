#!/usr/bin/python3
from flask import Flask
from flask import jsonify
import json


# Instantiate the Flask app
app = Flask(__name__)
users = {}

# Define a route for the root URL
@app.route("/")
def home():
    return "Welcome to the Flask API!"
@app.route("/data")
def data():
    return jsonify()
@app.route("/status")
def status():
    return "OK"
# Run the development server
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    if not user_data or 'username' not in user_data:
        return jsonify({"error": "Invalid data or missing username"}), 400
    
    username = user_data['username']
    
    # Add the user data to the users dictionary
    users[username] = {
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    
    return jsonify({"message": "User added successfully", "user": users[username]}), 201

if __name__ == "__main__":
    app.run()