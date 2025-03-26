from flask import Flask, request, jsonify
from flask_cors import CORS

from HyperPersonalization.backend.DataScraper import fetch_user_details_by_userName
from HyperPersonalization.backend.remommendation_Generator import get_recommendations

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
    global user_data
    try:
        data = request.get_json()

        if not data:
            return jsonify({"message": "No data received"}), 400

        username = data.get('username')
        if not username:
            return jsonify({"message": "No username provided"}), 400

        selected_username = username
        user_data = fetch_user_details_by_userName(selected_username)
        print("✅ Selected user data:", user_data)
        print(type(user_data))
        if "error" in user_data:
            return jsonify({"message": f"User '{username}' not found in the backend"}), 404
        else:
            return jsonify({"message": f"User '{username}' found in the backend"}), 200

    except Exception as e:
        print("❌ Error in /submit:", e.with_traceback())
        return jsonify({"message": "Something went wrong on the server"}), 500

@app.route('/recommend', methods=['GET'])
def get_recommendation():
    try:
        if not selected_username:
            return jsonify({"message": "No user submitted yet."}), 400
        print("user:", selected_username)
        # Dummy recommendation list (can be replaced with actual logic)
        recommendations = get_recommendations(user_data)
        print("--------------------------------------------------------------")
        print("recommendation:", recommendations)
        print("frintend:  ", jsonify(recommendations),200)
        return jsonify(recommendations)

    except Exception as e:
        print("❌ Error in /recommend:", e)
        return jsonify({"message": "Something went wrong on the server"}), 500

if __name__ == '__main__':
    app.run(debug=True)
