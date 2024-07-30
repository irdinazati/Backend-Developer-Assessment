"""
Task 6: Error Handling Implement appropriate error handling mechanisms 
for the API to handle scenarios like invalid input, missing resources, etc.
"""

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

@app.route('/funds', methods=['POST'])
def create_fund():
    data = request.json
    if not data or not all(key in data for key in ('fund_id', 'fund_name', 'fund_manager_name', 'fund_description', 'fund_nav', 'fund_date_of_creation', 'fund_performance')):
        abort(400)
    new_fund = Fund(
        fund_id=data['fund_id'],
        fund_name=data['fund_name'],
        fund_manager_name=data['fund_manager_name'],
        fund_description=data['fund_description'],
        fund_nav=data['fund_nav'],
        fund_date_of_creation=data['fund_date_of_creation'],
        fund_performance=data['fund_performance']
    )
    try:
        db.session.add(new_fund)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500)
    return jsonify(new_fund.to_dict()), 201
