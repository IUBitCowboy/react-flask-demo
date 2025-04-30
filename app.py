from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS to allow requests from your React frontend
CORS(app)


@app.route('/api/users', methods=['GET'])
def get_user_count():
    # Add debugging output
    # print("Received request for /api/users")
    # print(f"Request headers: {request.headers}")

    # In a real application, you would query a database or perform other business logic here
    # For this example, we'll just return a hardcoded value
    return jsonify({"Users": 2})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')