#!/usr/bin/python3
from flask import Flask, jsonify, request

# Instantiate the Flask app
app = Flask(__name__)

# In-memory dictionary to store user data
users = {}

# Define a route for the root URL
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route to return some data
@app.route("/data")
def data():
        userlist = list(users.keys())
        return jsonify(userlist), 200
# Route for status check
@app.route("/status")
def status():
    return "OK"

# Dynamic route to get a user by username
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route to add a new user via POST request
@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400
    
    
    # Add the user data to the users dictionary
    nuevo = {
        "username": user_data['username'],
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    
    users[nuevo['username']] = nuevo
    return jsonify({"message": "User added", "user": nuevo}), 201

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)