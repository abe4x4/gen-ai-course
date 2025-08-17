"""
utils.py
Step 6: Utility functions for NLP projects
"""

import pandas as pd

# =============================
# Load dataset from CSV
# =============================
def load_csv(file_path):
    """
    Load a CSV file and return a pandas DataFrame
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} rows from {file_path}")
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

# =============================
# Print model results
# =============================
from sklearn.metrics import confusion_matrix, classification_report

def print_results(y_true, y_pred):
    """
    Print confusion matrix and classification report
    """
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))

# =============================
# Example: Save predictions to CSV
# =============================
def save_predictions(sentences, predictions, file_path="predictions.csv"):
    """
    Save predictions in a CSV file
    """
    df = pd.DataFrame({"Sentence": sentences, "Prediction": predictions})
    df.to_csv(file_path, index=False)
    print(f"Saved predictions to {file_path}")
