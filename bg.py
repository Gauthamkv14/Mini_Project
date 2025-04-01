from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend interaction

# In-memory storage for reports and donations
reports = []
donations = []

# Endpoint to submit a report
@app.route('/api/reports', methods=['POST'])
def submit_report():
    data = request.get_json()
    report = data.get('report')
    if not report:
        return jsonify({'message': 'Report is required'}), 400
    reports.append(report)
    print('Report received:', report)
    return jsonify({'message': 'Report submitted successfully'}), 201

# Endpoint to get all reports
@app.route('/api/reports', methods=['GET'])
def get_reports():
    return jsonify({'reports': reports})

# Endpoint to submit a donation
@app.route('/api/donations', methods=['POST'])
def submit_donation():
    data = request.get_json()
    item = data.get('item')
    quantity = data.get('quantity')
    if not item or not quantity:
        return jsonify({'message': 'Item and quantity are required'}), 400
    donations.append({'item': item, 'quantity': quantity})
    print('Donation received:', {'item': item, 'quantity': quantity})
    return jsonify({'message': 'Donation submitted successfully'}), 201

# Endpoint to get all donations
@app.route('/api/donations', methods=['GET'])
def get_donations():
    return jsonify({'donations': donations})

# Start the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)