"""
basics_ds_ml.py
Step 3: Core Libraries for Data Science & Machine Learning
"""

# =============================
# 1. NUMPY
# =============================
import numpy as np

# Creating arrays
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Basic operations
print("Add 5:", arr + 5)
print("Square:", arr ** 2)
print("Sum:", np.sum(arr))

# Create 2D array
arr2d = np.array([[1,2,3],[4,5,6]])
print("2D Array:\n", arr2d)
print("Mean along axis 0:", np.mean(arr2d, axis=0))
print("Mean along axis 1:", np.mean(arr2d, axis=1))

# =============================
# 2. PANDAS
# =============================
import pandas as pd

# Create DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Salary": [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Access columns and rows
print("\nNames column:", df["Name"])
print("\nFirst two rows:\n", df.head(2))

# Basic statistics
print("\nSummary statistics:\n", df.describe())

# Filter data
print("\nPeople older than 30:\n", df[df["Age"] > 30])

# =============================
# 3. MATPLOTLIB
# =============================
import matplotlib.pyplot as plt

ages = df["Age"]
salaries = df["Salary"]

plt.scatter(ages, salaries)
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# =============================
# 4. SCIKIT-LEARN (Linear Regression Example)
# =============================
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Prepare data
X = df[["Age"]]        # Feature
y = df["Salary"]       # Target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
print("\nPredicted salaries:", predictions)
print("Actual salaries:", y_test.values)

# Evaluate model
r2_score = model.score(X_test, y_test)
print("R^2 score:", r2_score)
