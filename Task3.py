# Task 3: Data Persistence Implement data persistence using a lightweight database system (e.g., SQLite or JSON file). When a new fundis created or the performance of an existing fund is updated, the data should be stored persistently.

from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///funds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Fund model
class Fund(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fund_id = db.Column(db.String(10), unique=True, nullable=False)
    fund_name = db.Column(db.String(100), nullable=False)
    fund_manager_name = db.Column(db.String(100), nullable=False)
    fund_description = db.Column(db.String(200), nullable=False)
    fund_nav = db.Column(db.Float, nullable=False)
    fund_date_of_creation = db.Column(db.String(20), nullable=False)
    fund_performance = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'fund_id': self.fund_id,
            'fund_name': self.fund_name,
            'fund_manager_name': self.fund_manager_name,
            'fund_description': self.fund_description,
            'fund_nav': self.fund_nav,
            'fund_date_of_creation': self.fund_date_of_creation,
            'fund_performance': self.fund_performance
        }

# Initialize the database
with app.app_context():
    db.create_all()

# Route to get all funds
@app.route('/funds', methods=['GET'])
def get_funds():
    funds = Fund.query.all()
    return jsonify([fund.to_dict() for fund in funds])

@app.route('/funds/add', methods=['POST'])
def create_fund():
    data = request.json
    new_fund = Fund(
        fund_id=data['fund_id'],
        fund_name=data['fund_name'],
        fund_manager_name=data['fund_manager_name'],
        fund_description=data['fund_description'],
        fund_nav=data['fund_nav'],
        fund_date_of_creation=data['fund_date_of_creation'],
        fund_performance=data['fund_performance']
    )
    db.session.add(new_fund)
    db.session.commit()
    return jsonify(new_fund.to_dict()), 201


# Route to get a specific fund by fund_id
@app.route('/funds/<fund_id>', methods=['GET'])
def get_fund(fund_id):
    fund = Fund.query.filter_by(fund_id=fund_id).first()
    if fund is None:
        abort(404)
    return jsonify(fund.to_dict())

# Route to update a fund's performance
@app.route('/funds/<fund_id>', methods=['PUT'])
def update_fund(fund_id):
    data = request.json
    fund = Fund.query.filter_by(fund_id=fund_id).first()
    if fund is None:
        abort(404)
    fund.fund_performance = data['fund_performance']
    db.session.commit()
    return jsonify(fund.to_dict())

# Route to delete a fund by fund_id
@app.route('/funds/<fund_id>', methods=['DELETE'])
def delete_fund(fund_id):
    fund = Fund.query.filter_by(fund_id=fund_id).first()
    if fund is None:
        abort(404)
    db.session.delete(fund)
    db.session.commit()
    return jsonify({'message': 'Fund deleted'})

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
