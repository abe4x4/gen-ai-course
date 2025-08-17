"""
sql_queries.py
Step 4: Practice SQL queries with Python
"""

import sqlite3

# Connect to the database
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# =============================
# 1. SELECT QUERY
# =============================
print("All Employees:")
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

# =============================
# 2. FILTER DATA
# =============================
print("\nEmployees in IT department:")
cursor.execute("SELECT * FROM employees WHERE department = 'IT'")
for row in cursor.fetchall():
    print(row)

# =============================
# 3. JOIN QUERY
# =============================
print("\nEmployee names with salaries:")
cursor.execute('''
SELECT e.name, s.salary
FROM employees e
JOIN salaries s ON e.id = s.employee_id
''')
for row in cursor.fetchall():
    print(row)

# =============================
# 4. UPDATE QUERY
# =============================
print("\nUpdating salary of Alice to 52000")
cursor.execute("UPDATE salaries SET salary = 52000 WHERE employee_id = 1")
conn.commit()

# =============================
# 5. DELETE QUERY
# =============================
print("\nDeleting employee Eve")
cursor.execute("DELETE FROM employees WHERE name = 'Eve'")
conn.commit()

# Close connection
conn.close()
