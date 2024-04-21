import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Indexer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.inverted_index = {}
        self.documents = []

    def add_document(self, doc_id, text):
        self.documents.append(text)
        doc_index = len(self.documents) - 1
        for term in set(text.split()):
            if term not in self.inverted_index:
                self.inverted_index[term] = []
            self.inverted_index[term].append((doc_id, doc_index))

    def build_index(self):
        tfidf_matrix = self.vectorizer.fit_transform(self.documents)
        self.tfidf_matrix = tfidf_matrix

    def save_index(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump((self.inverted_index, self.tfidf_matrix), file)

    def load_index(self, filename):
        with open(filename, 'rb') as file:
            self.inverted_index, self.tfidf_matrix = pickle.load(file)

    def search(self, query, k=5):
        query_vector = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        # Retrieve TF-IDF scores for the query
        query_tfidf_scores = query_vector.toarray().flatten()
        doc_scores = [(doc_id, cosine_score, tfidf_score) for doc_id, (cosine_score, tfidf_score) in enumerate(zip(cosine_similarities, query_tfidf_scores))]
        doc_scores.sort(key=lambda x: x[1], reverse=True)
        return doc_scores[:k]

