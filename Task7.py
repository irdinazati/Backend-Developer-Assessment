"""
Task 7: Testing Write test cases to ensure the proper functioning of both the API endpoints and the SQL database. The tests should
cover various scenarios and edge cases, including testing the SQL queries and verifying data integrity in the database.
"""

import unittest
from app import app, db, Fund

class FundAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_fund(self):
        response = self.app.post('/funds', json={
            'fund_id': 'F01',
            'fund_name': 'Test Fund',
            'fund_manager_name': 'John Doe',
            'fund_description': 'A test fund',
            'fund_nav': 1000000,
            'fund_date_of_creation': '2024-07-26',
            'fund_performance': 10.5
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Fund', response.get_data(as_text=True))

    def test_get_fund(self):
        response = self.app.post('/funds', json={
            'fund_id': 'F02',
            'fund_name': 'Test Fund 2',
            'fund_manager_name': 'Jane Doe',
            'fund_description': 'Another test fund',
            'fund_nav': 2000000,
            'fund_date_of_creation': '2024-07-26',
            'fund_performance': 15.5
        })
        self.assertEqual(response.status_code, 201)

        response = self.app.get('/funds/F02')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Fund 2', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
