"""
train_model.py
Step 5: Training a simple feedforward neural network
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from neural_network import NeuralNetwork

# =============================
# 1. Load Dataset
# =============================
iris = load_iris()
X = iris.data  # Features
y = iris.target.reshape(-1, 1)  # Labels

# One-hot encode the labels
encoder = OneHotEncoder(sparse=False)
y_encoded = encoder.fit_transform(y)

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# =============================
# 2. Initialize and Train Model
# =============================
input_size = X_train.shape[1]  # 4 features
hidden_size = 5
output_size = y_train.shape[1]  # 3 classes

nn = NeuralNetwork(input_size, hidden_size, output_size, learning_rate=0.1)
nn.train(X_train, y_train, epochs=1000)

# =============================
# 3. Evaluate Model
# =============================
predictions = nn.forward(X_test)
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)

accuracy = np.mean(predicted_classes == true_classes)
print(f"\nTest Accuracy: {accuracy*100:.2f}%")
