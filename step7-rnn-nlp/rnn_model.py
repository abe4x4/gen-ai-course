"""
rnn_model.py
Step 7: Recurrent Neural Network for next-word prediction
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense, LSTM
from dataset_loader import X, y, max_sequence_len, total_words

# =============================
# Build the RNN model
# =============================
model = Sequential()
model.add(Embedding(input_dim=total_words, output_dim=10, input_length=max_sequence_len-1))
model.add(SimpleRNN(50))  # Simple RNN layer
# model.add(LSTM(50))     # Alternatively, you can try LSTM instead of SimpleRNN
model.add(Dense(total_words, activation='softmax'))

# =============================
# Compile model
# =============================
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# =============================
# Train the model
# =============================
model.fit(X, y, epochs=200, verbose=1)

# =============================
# Predict next word
# =============================
def predict_next_word(model, tokenizer, text, max_sequence_len):
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    import numpy as np
    
    token_list = tokenizer.texts_to_sequences([text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted = model.predict(token_list, verbose=0)
    predicted_word_index = np.argmax(predicted, axis=-1)[0]
    
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return None

# Example usage
seed_text = "I love"
next_word = predict_next_word(model, dataset_loader.tokenizer, seed_text, max_sequence_len)
print(f"{seed_text} -> {next_word}")
