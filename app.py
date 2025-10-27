from flask import Flask, jsonify, request

app = Flask(__name__)


users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]


# GET - Retrieve all users

@app.route('/', methods=['GET'])
def get_users():
    return jsonify(users), 200


# GET - Retrieve single user

@app.route('/', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404


# POST - Add new user

@app.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and Email are required"}), 400

    new_id = users[-1]["id"] + 1 if users else 1
    new_user = {"id": new_id, "name": data["name"], "email": data["email"]}
    users.append(new_user)
    return jsonify(new_user), 201


# PUT - Update user

@app.route('/', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200


# DELETE - Remove user

@app.route('/', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": f"User {user_id} deleted"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
