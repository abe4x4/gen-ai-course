"""
sentiment_analysis.py
Step 6: Sentiment Analysis with NLP
"""

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from preprocess import preprocess_pipeline

# =============================
# Sample Dataset
# =============================
# In real scenarios, replace this with a real dataset (CSV, API, etc.)
texts = [
    "I love this product, it works amazingly!",
    "This is the worst experience I ever had.",
    "Absolutely fantastic, I will buy again.",
    "Terrible, very disappointing.",
    "I am so happy with this purchase.",
    "I hate it, totally useless."
]

labels = [1, 0, 1, 0, 1, 0]  # 1 = Positive, 0 = Negative

# =============================
# Preprocess Text
# =============================
processed_texts = [" ".join(preprocess_pipeline(text)) for text in texts]

# =============================
# Train/Test Split
# =============================
X_train, X_test, y_train, y_test = train_test_split(
    processed_texts, labels, test_size=0.33, random_state=42
)

# =============================
# Vectorization
# =============================
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# =============================
# Train Classifier
# =============================
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# =============================
# Evaluate Model
# =============================
y_pred = model.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# =============================
# Test with New Sentences
# =============================
new_sentences = [
    "I really enjoyed this, highly recommend it!",
    "Not worth the money, very bad."
]

new_processed = [" ".join(preprocess_pipeline(s)) for s in new_sentences]
new_vec = vectorizer.transform(new_processed)
new_pred = model.predict(new_vec)

for sentence, pred in zip(new_sentences, new_pred):
    label = "Positive" if pred == 1 else "Negative"
    print(f"'{sentence}' -> {label}")
