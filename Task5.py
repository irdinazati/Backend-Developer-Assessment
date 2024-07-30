"""
Task 5: SQL Data Migration Write SQL scripts to migrate the data from the 
lightweight database system (used for Task 3) 
to the SQLdatabase you designed in Task 4
"""
import sqlite3

# Define database file names
old_db_file = 'funds.db'
new_db_file = 'new_funds.db'

# Step 1: Migrate Data from Old SQLite Database to New SQLite Database
def migrate_data(old_db_file, new_db_file):
    # Connect to the old SQLite database
    old_conn = sqlite3.connect(old_db_file)
    old_cursor = old_conn.cursor()
    
    # Connect to the new SQLite database
    new_conn = sqlite3.connect(new_db_file)
    new_cursor = new_conn.cursor()

    # Create the table in the new database
    new_cursor.execute('''
    CREATE TABLE IF NOT EXISTS funds (
        fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fund_name TEXT NOT NULL,
        fund_manager_name TEXT NOT NULL,
        fund_description TEXT NOT NULL,
        fund_nav REAL NOT NULL,
        fund_date_of_creation TEXT NOT NULL,
        fund_performance REAL NOT NULL
    )
    ''')

    # Fetch all data from the old database
    old_cursor.execute("SELECT * FROM funds")
    funds = old_cursor.fetchall()
    
    # Insert data into the new database
    for fund in funds:
        new_cursor.execute('''
        INSERT INTO funds (fund_name, fund_manager_name, fund_description, fund_nav, fund_date_of_creation, fund_performance)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (fund[1], fund[2], fund[3], fund[4], fund[5], fund[6]))

    # Commit changes and close the connections
    new_conn.commit()
    old_conn.close()
    new_conn.close()
    print(f"Data migrated from {old_db_file} to {new_db_file}")

if __name__ == '__main__':
    migrate_data(old_db_file, new_db_file)
