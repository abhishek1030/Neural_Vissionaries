from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Store username temporarily in memory
selected_username = ""

@app.route('/')
def home():
    return "Backend is running"

@app.route('/submit', methods=['POST'])
def submit_user():
    global selected_username
    try:
        data = request.get_json()

        if not data:
            return jsonify({"message": "No data received"}), 400

        username = data.get('username')
        if not username:
            return jsonify({"message": "No username provided"}), 400

        selected_username = username
        print("✅ Selected username:", username)

        return jsonify({"message": f"User '{username}' received by backend"}), 200

    except Exception as e:
        print("❌ Error in /submit:", e)
        return jsonify({"message": "Something went wrong on the server"}), 500

@app.route('/recommend', methods=['GET'])
def get_recommendation():
    try:
        if not selected_username:
            return jsonify({"message": "No user submitted yet."}), 400

        # Dummy recommendation list (can be replaced with actual logic)
        recommendations = [
            {"item": f"Recommended Item 1 for {selected_username}", "score": 0.92},
            {"item": f"Recommended Item 2 for {selected_username}", "score": 0.88},
            {"item": f"Recommended Item 3 for {selected_username}", "score": 0.81}
        ]

        return jsonify(recommendations), 200

    except Exception as e:
        print("❌ Error in /recommend:", e)
        return jsonify({"message": "Something went wrong on the server"}), 500

if __name__ == '__main__':
    app.run(debug=True)
