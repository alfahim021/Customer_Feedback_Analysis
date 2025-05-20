# scripts/feedback_analysis.py

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

def download_nltk_resources():
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')

def clean_text(text, stop_words, lemmatizer):
    if pd.isnull(text):
        return ""
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)

def get_sentiment(text):
    if text == "":
        return "neutral"
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

def main():
    # Download required NLTK data
    download_nltk_resources()

    # File paths - update if needed
    input_file = '../data/raw/redmi6.csv'
    output_csv = '../data/processed/customer_feedback_with_sentiments.csv'
    output_excel = '../data/processed/customer_feedback_with_sentiments.xlsx'

    # Load raw data
    df = pd.read_csv(input_file, encoding='cp1252')

    # Define feedback column name (from your dataset)
    feedback_col = 'Comments'

    # Prepare stopwords and lemmatizer
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # Clean the feedback text
    df['cleaned_review'] = df[feedback_col].apply(lambda x: clean_text(x, stop_words, lemmatizer))

    # Perform sentiment analysis
    df['sentiment'] = df['cleaned_review'].apply(get_sentiment)

    # Save cleaned data with sentiment labels
    df.to_csv(output_csv, index=False)
    df.to_excel(output_excel, index=False)

    # Print sentiment distribution summary
    print("Sentiment distribution:")
    print(df['sentiment'].value_counts())

if __name__ == "__main__":
    main()
 Python script for data cleaning and sentiment analysis
