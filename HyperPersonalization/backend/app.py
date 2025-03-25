from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory user storage
submitted_users = {}

@app.route('/submit', methods=['POST'])
def submit_user():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'message': 'Username is required'}), 400

    # Store user (mock)
    submitted_users[username] = f"Recommendation for {username}"
    return jsonify({'message': f'User {username} submitted successfully'}), 200

@app.route('/recommendation', methods=['GET'])
def get_recommendation():
    username = request.args.get('username')
    if not username or username not in submitted_users:
        return jsonify({'error': 'User not found'}), 404

    # Return stored recommendation
    recommendation = submitted_users[username]
    return jsonify({'recommendation': recommendation})

if __name__ == '__main__':
    app.run(debug=True)