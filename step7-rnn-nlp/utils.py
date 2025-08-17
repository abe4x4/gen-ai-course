"""
utils.py
Optional utility functions for NLP and RNN projects (Step 7)
"""

import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

# =============================
# CSV Dataset Loader
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
# Print classification results
# =============================
def print_results(y_true, y_pred):
    """
    Print confusion matrix and classification report
    """
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))

# =============================
# Save predictions to CSV
# =============================
def save_predictions(texts, predictions, file_path="predictions.csv"):
    """
    Save predictions or generated words to CSV
    """
    df = pd.DataFrame({"Input": texts, "Prediction": predictions})
    df.to_csv(file_path, index=False)
    print(f"Saved predictions to {file_path}")

# =============================
# Convert RNN prediction to word
# =============================
def index_to_word(pred_index, tokenizer):
    """
    Convert predicted index from RNN model to word
    """
    for word, index in tokenizer.word_index.items():
        if index == pred_index:
            return word
    return None
