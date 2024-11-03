from flask import Blueprint, jsonify, request
from src import analysis
from src import analysis_of_feelings

main = Blueprint('main', __name__)

@main.route("/analyze", methods=["POST"])
def analyze():
    # Extract JSON data from request body
    body = request.get_json()
    
    # Check if 'text' is in the body
    if not body or "text" not in body:
        return jsonify({"error": "Missing 'text' field"}), 400
    
    # Access the 'text' field from the JSON body
    text_to_analyze = body["text"]
    
    # Assuming there's a function analyze_data that processes this text
    User = analysis.analyze_data(text_to_analyze)
    
    # Return a JSON response with the processed data or a confirmation message
    return User.to_dict(), 200

