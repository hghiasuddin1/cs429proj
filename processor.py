from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

class QueryProcessor:
    def __init__(self, documents):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(documents)

    def process_query(self, query, k=5):
        # Validate query
        if not query:
            return {'error': 'Query is empty'}
        
        # Transform query into TF-IDF vector
        query_vector = self.vectorizer.transform([query])

        # Calculate cosine similarity between query vector and document vectors
        similarity_scores = cosine_similarity(query_vector, self.tfidf_matrix)[0]
        
        # Sort documents by similarity scores and return top-K results
        top_k_indices = similarity_scores.argsort()[-k:][::-1]
        top_k_results = [{'document_index': idx, 'similarity_score': similarity_scores[idx]} for idx in top_k_indices]

        return {'results': top_k_results}

# Example documents
documents = ["document1 content", "document2 content", "document3 content"]
processor = QueryProcessor(documents)

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({'error': 'Query is missing in JSON data'}), 400
    
    # Process query and return top-K results
    results = processor.process_query(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
