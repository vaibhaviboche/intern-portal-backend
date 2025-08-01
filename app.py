from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/intern-info')
def intern_info():
    data = {
        "name": "Vaibhavi Boche",
        "referral_code": "vaibhavi2025",
        "donations": 15420
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
