"""
database_setup.py
Step 4: SQL for Data Handling
This script creates a SQLite database with some sample tables and data
"""

import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# =============================
# 1. Create Tables
# =============================

# Employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
''')

# Salaries table
cursor.execute('''
CREATE TABLE IF NOT EXISTS salaries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    salary REAL,
    FOREIGN KEY (employee_id) REFERENCES employees (id)
)
''')

# =============================
# 2. Insert Sample Data
# =============================

employees_data = [
    ("Alice", 25, "IT"),
    ("Bob", 30, "HR"),
    ("Charlie", 35, "IT"),
    ("David", 40, "Finance"),
    ("Eve", 28, "HR")
]

salaries_data = [
    (1, 50000),
    (2, 60000),
    (3, 70000),
    (4, 80000),
    (5, 55000)
]

cursor.executemany('INSERT INTO employees (name, age, department) VALUES (?, ?, ?)', employees_data)
cursor.executemany('INSERT INTO salaries (employee_id, salary) VALUES (?, ?)', salaries_data)

# Commit and close
conn.commit()
conn.close()

print("Database and tables created successfully with sample data.")
