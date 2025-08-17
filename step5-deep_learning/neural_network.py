"""
neural_network.py
Step 5: Simple Feedforward Neural Network from Scratch
"""

import numpy as np
from utils import sigmoid, sigmoid_derivative, mse_derivative

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        # Initialize weights and biases
        self.learning_rate = learning_rate
        self.weights_input_hidden = np.random.randn(input_size, hidden_size) * 0.1
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.randn(hidden_size, output_size) * 0.1
        self.bias_output = np.zeros((1, output_size))

    def forward(self, X):
        """Forward pass"""
        self.input = X
        self.hidden_input = np.dot(self.input, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.output = sigmoid(self.output_input)
        return self.output

    def backward(self, y_true):
        """Backward pass with gradient descent"""
        # Calculate output error
        output_error = mse_derivative(y_true, self.output) * sigmoid_derivative(self.output_input)

        # Calculate hidden layer error
        hidden_error = np.dot(output_error, self.weights_hidden_output.T) * sigmoid_derivative(self.hidden_input)

        # Update weights and biases
        self.weights_hidden_output -= self.learning_rate * np.dot(self.hidden_output.T, output_error)
        self.bias_output -= self.learning_rate * np.sum(output_error, axis=0, keepdims=True)
        self.weights_input_hidden -= self.learning_rate * np.dot(self.input.T, hidden_error)
        self.bias_hidden -= self.learning_rate * np.sum(hidden_error, axis=0, keepdims=True)

    def train(self, X, y, epochs=1000):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(y)
            if (epoch + 1) % 100 == 0:
                loss = np.mean((y - output) ** 2)
                print(f"Epoch {epoch+1}/{epochs}, Loss: {loss:.4f}")
