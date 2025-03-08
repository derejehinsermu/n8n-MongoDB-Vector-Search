import os
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load Hugging Face model with 768-dimensional embeddings
embedding_model = SentenceTransformer("BAAI/bge-base-en-v1.5")

@app.route('/generate_embedding', methods=['POST'])
def generate_embedding():
    request_data = request.json
    if not request_data or not request_data.get("text", "").strip():
        return jsonify({"success": False, "message": "Text field is empty or missing"}), 400

    text = request_data["text"]

    try:
        # Generate embedding using Hugging Face model
        embedding = embedding_model.encode(text).tolist()
        return jsonify({"success": True, "embedding": embedding})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
