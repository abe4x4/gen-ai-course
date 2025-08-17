# Step 6: Natural Language Processing (NLP)

In this step, you learn how to **handle text data** and perform **basic sentiment analysis**.

---

## Topics Covered

### 1. Text Preprocessing
- Cleaning text (lowercasing, removing punctuation/numbers)
- Tokenization
- Stopwords removal
- Full preprocessing pipeline (`preprocess_pipeline` in `preprocess.py`)

### 2. Vectorization
- `CountVectorizer` to convert text to numerical features
- Prepare text data for ML models

### 3. Sentiment Analysis
- Train/test split
- Naive Bayes classifier (`MultinomialNB`)
- Accuracy and classification report
- Predicting new examples

### 4. Optional Utilities (`utils.py`)
`utils.py` contains helper functions that make your workflow cleaner and more modular:
- Load CSV files easily with `load_csv()`
- Print model results neatly with `print_results()`
- Save predictions to CSV using `save_predictions()`

**Why use `utils.py`?**
- Keeps your main scripts (`sentiment_analysis.py`) clean and focused on core logic.
- Makes it easier to reuse functions across different steps/projects.
- Encourages modular, professional coding practices that scale for bigger NLP or generative AI projects.

---

## Instructions

1. Run `sentiment_analysis.py` to train and test the sentiment analysis model.
2. Modify `texts` to try with your own sentences.
3. Optional: Use `utils.py` functions to:
   - Load datasets fro
