from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Initialize TF-IDF vectorizer and document matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = None

# Route for adding documents
@app.route('/add_documents', methods=['POST'])
def add_documents():
    global tfidf_matrix
    
    # Get JSON data from request
    data = request.json
    
    # Extract documents from JSON data
    documents = data.get('documents')
    
    if not documents:
        return jsonify({'error': 'No documents provided'}), 400
    
    # Update TF-IDF matrix with new documents
    if tfidf_matrix is None:
        tfidf_matrix = vectorizer.fit_transform(documents)
    else:
        tfidf_matrix = vectorizer.transform(documents)
    
    return jsonify({'message': 'Documents added successfully'})

# Route for processing queries
@app.route('/query', methods=['POST'])
def process_query():
    global tfidf_matrix
    
    # Get JSON data from request
    data = request.json
    
    # Check if the 'query' key is present in the JSON data
    if 'query' not in data:
        return jsonify({'error': 'Query key is missing in JSON data'}), 400
    
    # Extract query from JSON data
    query = data['query']
    
    # Validate the query
    if not query.strip():
        return jsonify({'error': 'Query is empty or contains only whitespace'}), 400
    
    # Check if TF-IDF matrix is initialized
    if tfidf_matrix is None:
        return jsonify({'error': 'No documents added yet. Please add documents before querying'}), 400
    
    # Vectorize the query
    query_vector = vectorizer.transform([query])
    
    # Calculate cosine similarity between query vector and document vectors
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    # Sort documents by similarity scores and return top-K results
    k = data.get('top_k', 5)
    top_k_indices = similarity_scores.argsort()[-k:][::-1]
    top_k_results = [{'document_index': int(idx), 'similarity_score': float(similarity_scores[idx])} for idx in top_k_indices]
    
    return jsonify({'results': top_k_results})

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
