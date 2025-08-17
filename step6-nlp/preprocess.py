"""
preprocess.py
Step 6: Text preprocessing for NLP
"""

import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK resources (run once)
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# =============================
# Text Cleaning
# =============================
def clean_text(text):
    """
    Clean text by:
    - Lowercasing
    - Removing punctuation
    - Removing numbers
    """
    text = text.lower()  # Lowercase
    text = re.sub(f"[{string.punctuation}]", "", text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove numbers
    return text

# =============================
# Tokenization
# =============================
def tokenize_text(text):
    """
    Tokenize text into words
    """
    return word_tokenize(text)

# =============================
# Stopwords Removal
# =============================
def remove_stopwords(tokens):
    """
    Remove common stopwords (e.g., 'the', 'is', 'and')
    """
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

# =============================
# Complete Preprocessing Pipeline
# =============================
def preprocess_pipeline(text):
    """
    Full preprocessing: clean, tokenize, remove stopwords
    """
    cleaned = clean_text(text)
    tokens = tokenize_text(cleaned)
    filtered_tokens = remove_stopwords(tokens)
    return filtered_tokens
