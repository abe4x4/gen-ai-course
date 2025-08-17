### Optional Utilities (`utils.py`)
`utils.py` contains reusable helper functions for Step 7:
- Load CSV datasets with `load_csv()`
- Print evaluation metrics with `print_results()`
- Save predictions to CSV using `save_predictions()`
- Convert model prediction index to word using `index_to_word()`

**Why use `utils.py`?**
- Keeps your main scripts (`rnn_model.py`) clean and focused on model logic
- Allows reuse of functions for text generation, RNN evaluation, or future steps (e.g., Transformers)
- Optional: you can skip it, but it’s recommended for professional, modular code

**Example Usage in `rnn_model.py`:**
```python
from utils import save_predictions, index_to_word

# Save predicted words for a list of seed texts
pred_words = [index_to_word(np.argmax(model.predict(x)), tokenizer) for x in X_samples]
save_predictions(seed_texts, pred_words)
