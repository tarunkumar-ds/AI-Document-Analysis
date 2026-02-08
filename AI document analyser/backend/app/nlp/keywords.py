from sklearn.feature_extraction.text import TfidfVectorizer
import re
def extract_keywords(text, top_k=10):
    words = re.findall(r"[a-zA-Z]{3,}", text.lower())

    if len(words) < 10:
        return list(set(words))[:top_k]

    try:
        vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=100
        )
        tfidf = vectorizer.fit_transform([text])

        return vectorizer.get_feature_names_out()[:top_k].tolist()

    except ValueError:
        return list(set(words))[:top_k]

