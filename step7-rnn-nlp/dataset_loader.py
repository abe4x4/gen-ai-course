"""
dataset_loader.py
Step 7: Load and preprocess text dataset for RNN
"""

import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample dataset: short sentences
texts = [
    "I love machine learning",
    "I love deep learning",
    "I enjoy learning new things",
    "Machine learning is amazing",
    "Deep learning models are powerful"
]

# =============================
# Tokenization
# =============================
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
total_words = len(tokenizer.word_index) + 1  # total vocabulary size

# =============================
# Create input sequences for RNN
# =============================
input_sequences = []

for line in texts:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

# =============================
# Pad sequences
# =============================
max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

# =============================
# Create predictors and label
# =============================
X = input_sequences[:,:-1]
y = input_sequences[:,-1]

from tensorflow.keras.utils import to_categorical
y = to_categorical(y, num_classes=total_words)

print(f"Total words: {total_words}")
print(f"Example X[0]: {X[0]}")
print(f"Example y[0]: {y[0]}")
