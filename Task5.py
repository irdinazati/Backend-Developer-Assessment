"""
Task 5: SQL Data Migration Write SQL scripts to migrate the data from the 
lightweight database system (used for Task 3) 
to the SQLdatabase you designed in Task 4
"""
import sqlite3

def migrate_data(old_db_path='old_funds.db', new_db_path='funds.db'):
    old_conn = sqlite3.connect(old_db_path)
    new_conn = sqlite3.connect(new_db_path)
    old_cursor = old_conn.cursor()
    new_cursor = new_conn.cursor()

    old_cursor.execute("SELECT * FROM investment_funds")
    funds = old_cursor.fetchall()

    for fund in funds:
        new_cursor.execute("""
            INSERT INTO investment_funds (fund_id, fund_name, fund_manager_name, fund_description, fund_nav, fund_date_of_creation, fund_performance)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, fund[1:])

    new_conn.commit()
    old_conn.close()
    new_conn.close()

migrate_data()

