/*Task 4: SQL Database Schema Design an appropriate database schema to store investment fund data. Create SQL statements to create
the necessary tables and relationships.*/

CREATE TABLE fund (
    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_name TEXT NOT NULL,
    fund_manager_name TEXT NOT NULL,
    fund_description TEXT NOT NULL,
    fund_nav REAL NOT NULL,
    fund_date_of_creation TEXT NOT NULL,
    fund_performance REAL NOT NULL
);