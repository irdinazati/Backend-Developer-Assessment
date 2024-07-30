"""
Task 7: Testing Write test cases to ensure the proper functioning of both the API endpoints and the SQL database. The tests should
cover various scenarios and edge cases, including testing the SQL queries and verifying data integrity in the database.
"""

import pytest
from Task3 import app, db, Fund

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_funds.db'
    client = app.test_client()

    # Create tables and initialize the database
    with app.app_context():
        db.create_all()

    yield client

    # Drop tables after tests
    with app.app_context():
        db.drop_all()

def test_create_fund(client):
    response = client.post('/funds/add', json={
        'fund_id': '1',  # Ensure fund_id is included
        'fund_name': 'Growth Fund',
        'fund_manager_name': 'Irdina Izzati',
        'fund_description': 'A high-growth fund',
        'fund_nav': 100.0,
        'fund_date_of_creation': '2024-07-30',
        'fund_performance': 5.0
    })
    assert response.status_code == 201
    assert b'Growth Fund' in response.data

def test_get_fund(client):
    client.post('/funds/add', json={
        'fund_id': '1',  # Ensure fund_id is included
        'fund_name': 'Growth Fund',
        'fund_manager_name': 'Irdina Izzati',
        'fund_description': 'A high-growth fund',
        'fund_nav': 100.0,
        'fund_date_of_creation': '2024-07-30',
        'fund_performance': 5.0
    })
    response = client.get('/funds/1')
    assert response.status_code == 200
    assert b'Growth Fund' in response.data

def test_update_fund(client):
    client.post('/funds/add', json={
        'fund_id': '1',  # Ensure fund_id is included
        'fund_name': 'Growth Fund',
        'fund_manager_name': 'Irdina Izzati',
        'fund_description': 'A high-growth fund',
        'fund_nav': 100.0,
        'fund_date_of_creation': '2024-07-30',
        'fund_performance': 5.0
    })
    response = client.put('/funds/1', json={'fund_performance': 10.0})
    assert response.status_code == 200
    assert b'10.0' in response.data

def test_delete_fund(client):
    client.post('/funds/add', json={
        'fund_id': '1',  # Ensure fund_id is included
        'fund_name': 'Growth Fund',
        'fund_manager_name': 'Irdina Izzati',
        'fund_description': 'A high-growth fund',
        'fund_nav': 100.0,
        'fund_date_of_creation': '2024-07-30',
        'fund_performance': 5.0
    })
    response = client.delete('/funds/1')
    assert response.status_code == 200
    assert b'Fund deleted' in response.data

def test_not_found(client):
    response = client.get('/funds/999')  # Assuming 999 is a non-existent ID
    assert response.status_code == 404

def test_bad_request(client):
    response = client.post('/funds/add', json={})
    assert response.status_code == 400
    assert b'Missing required fields' in response.data  # Adjust based on actual error message
