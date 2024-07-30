# Task 2: REST API Development Using Python and a web framework (Flask), create a RESTful API to manage investment funds.

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration purposes
funds = [
    {
        "fund_id": "F01",
        "fund_name": "Growth Fund",
        "fund_manager_name": "Irdina Izzati",
        "fund_description": "A fund focusing on growth stocks.",
        "fund_nav": 500000.0,
        "fund_date_of_creation": "2024-07-04",
        "fund_performance": 8.2
    }
]

# Endpoint to retrieve a list of all funds
@app.route('/funds', methods=['GET'])
def get_funds():
    return jsonify(funds), 200

# Endpoint to create a new fund
@app.route('/funds', methods=['POST'])
def create_fund():
    new_fund = request.json
    funds.append(new_fund)
    return jsonify(new_fund), 201

# Endpoint to retrieve details of a specific fund using its ID
@app.route('/funds/<fund_id>', methods=['GET'])
def get_fund(fund_id):
    fund = next((fund for fund in funds if fund["fund_id"] == fund_id), None)
    if fund is None:
        return jsonify({"error": "Fund not found"}), 404
    return jsonify(fund), 200

# Endpoint to update the performance of a fund using its ID
@app.route('/funds/<fund_id>', methods=['PUT'])
def update_fund(fund_id):
    fund = next((fund for fund in funds if fund["fund_id"] == fund_id), None)
    if fund is None:
        return jsonify({"error": "Fund not found"}), 404
    fund['fund_performance'] = request.json.get('fund_performance', fund['fund_performance'])
    return jsonify(fund), 200

# Endpoint to delete a fund using its ID
@app.route('/funds/<fund_id>', methods=['DELETE'])
def delete_fund(fund_id):
    global funds
    funds = [fund for fund in funds if fund["fund_id"] != fund_id]
    return jsonify({"message": "Fund deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
