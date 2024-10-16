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
    if users:
        return jsonify(users), 200
    else:
        return jsonify({"message": "No users found"}), 200
# Route for status check
@app.route("/status")
def status():
    return "OK"

# Dynamic route to get a user by username
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Route to add a new user via POST request
@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    if not user_data or 'username' not in user_data:
        return jsonify({"error": "Invalid data or missing username"}), 400
    
    username = user_data['username']
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    
    # Add the user data to the users dictionary
    users[username] = {
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    
    return jsonify({"message": "User added successfully", "user": users[username]}), 201

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)