"""
utils.py - Optional utilities for Step 3
"""

import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

# Load CSV
def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} rows from {file_path}")
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

# Print regression evaluation
def regression_results(y_true, y_pred):
    print(f"MSE: {mean_squared_error(y_true, y_pred)}")
    print(f"R^2: {r2_score(y_true, y_pred)}")
