from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome to AI Diary!"})

@main.route('/entries', methods=['GET'])
def get_entries():
    return jsonify({"entries": []})  # Placeholder for now
