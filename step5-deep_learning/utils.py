"""
utils.py
Step 5: Deep Learning Foundations - Utility functions
"""

import numpy as np

# =============================
# Activation Functions
# =============================
def sigmoid(x):
    """Sigmoid activation function"""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Derivative of sigmoid function for backpropagation"""
    return sigmoid(x) * (1 - sigmoid(x))

def relu(x):
    """ReLU activation function"""
    return np.maximum(0, x)

def relu_derivative(x):
    """Derivative of ReLU"""
    return (x > 0).astype(float)

# =============================
# Loss Function
# =============================
def mse(y_true, y_pred):
    """Mean Squared Error Loss"""
    return np.mean((y_true - y_pred) ** 2)

def mse_derivative(y_true, y_pred):
    """Derivative of MSE loss"""
    return 2 * (y_pred - y_true) / y_true.size

# =============================
# Accuracy
# =============================
def accuracy(y_true, y_pred):
    """Calculate accuracy for classification tasks"""
    predictions = np.argmax(y_pred, axis=1)
    labels = np.argmax(y_true, axis=1)
    return np.mean(predictions == labels)
