from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

class Indexer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.index = None

    def build_index(self, documents):
        # Convert documents into TF-IDF matrix
        tfidf_matrix = self.vectorizer.fit_transform(documents)
        
        # Compute cosine similarity matrix
        self.index = cosine_similarity(tfidf_matrix, tfidf_matrix)

    def save_index(self, filepath):
        if self.index:
            with open(filepath, 'wb') as f:
                pickle.dump(self.index, f)
            print(f"Inverted index saved to {filepath}")
        else:
            print("Error: Index is empty. Please build the index first.")

    def load_index(self, filepath):
        with open(filepath, 'rb') as f:
            self.index = pickle.load(f)
        print(f"Inverted index loaded from {filepath}")

# Example usage:
indexer = Indexer()
documents = ["document1 content", "document2 content", "document3 content"]
indexer.build_index(documents)
indexer.save_index("index.pkl")
loaded_index = indexer.load_index("index.pkl")
