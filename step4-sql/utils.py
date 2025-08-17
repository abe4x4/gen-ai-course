"""
utils.py - Optional utilities for Step 4
"""

import matplotlib.pyplot as plt

# Plot loss or accuracy
def plot_training(history, metric="loss"):
    plt.plot(history.history[metric])
    plt.title(f'Training {metric}')
    plt.xlabel('Epoch')
    plt.ylabel(metric)
    plt.show()
