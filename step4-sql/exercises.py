"""
exercises.py
Step 4: SQL Exercises
"""

import sqlite3

# Connect to the database
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# =============================
# Exercise 1: SELECT
# =============================
# Retrieve all employees older than 30
cursor.execute("SELECT * FROM employees WHERE age > 30")
print("Employees older than 30:")
for row in cursor.fetchall():
    print(row)

# =============================
# Exercise 2: JOIN
# =============================
# List employees with their salaries
cursor.execute('''
SELECT e.name, e.department, s.salary
FROM employees e
JOIN salaries s ON e.id = s.employee_id
''')
print("\nEmployees with their salaries:")
for row in cursor.fetchall():
    print(row)

# =============================
# Exercise 3: ADD NEW EMPLOYEE
# =============================
cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)", ("Frank", 33, "IT"))
cursor.execute("INSERT INTO salaries (employee_id, salary) VALUES (?, ?)", (6, 65000))
conn.commit()

# =============================
# Exercise 4: DELETE
# =============================
cursor.execute("DELETE FROM employees WHERE name = 'Bob'")
conn.commit()

conn.close()
