"""
exercises.py
Step 3: Data Science & ML Exercises
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# =============================
# 1. NUMPY EXERCISE
# =============================
# Create a 1D array with numbers 1 to 10
arr = np.arange(1, 11)
# Compute square and mean
print("Squares:", arr**2)
print("Mean:", np.mean(arr))

# =============================
# 2. PANDAS EXERCISE
# =============================
# Create DataFrame with columns: Name, Age, Salary, Department
data = {
    "Name": ["Alice","Bob","Charlie","David","Eve"],
    "Age": [25,30,35,40,28],
    "Salary": [50000,60000,70000,80000,55000],
    "Department": ["IT","HR","IT","Finance","HR"]
}
df = pd.DataFrame(data)

# Task: filter people in IT department older than 30
it_older_than_30 = df[(df["Department"]=="IT") & (df["Age"]>30)]
print("\nIT employees older than 30:\n", it_older_than_30)

# =============================
# 3. SIMPLE ML EXERCISE
# =============================
# Predict Salary from Age using Linear Regression
X = df[["Age"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("\nPredicted salaries:", predictions)
