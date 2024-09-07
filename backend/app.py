from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from collections import Counter
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    resume = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='Applied')

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Welcome to the Applicant Tracking System API"

@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content response for favicon

@app.route('/candidates', methods=['GET'])
def get_candidates():
    candidates = Candidate.query.all()
    result = [{'id': c.id, 'name': c.name, 'email': c.email, 'resume': c.resume, 'status': c.status} for c in candidates]
    return jsonify(result)

@app.route('/candidates/<int:id>', methods=['GET'])
def get_candidate(id):
    candidate = Candidate.query.get(id)
    if candidate:
        return jsonify({'id': candidate.id, 'name': candidate.name, 'email': candidate.email, 'resume': candidate.resume, 'status': candidate.status})
    return jsonify({'message': 'Candidate not found'}), 404

@app.route('/candidates', methods=['POST'])
def add_candidate():
    data = request.get_json()
    if 'name' not in data or 'email' not in data or 'resume' not in data:
        return jsonify({'message': 'Missing data'}), 400

    if Candidate.query.filter_by(email=data['email']).first() is not None:
        return jsonify({'message': 'Email already exists'}), 400

    new_candidate = Candidate(
        name=data['name'],
        email=data['email'],
        resume=data['resume'],
        status=data.get('status', 'Applied')
    )
    db.session.add(new_candidate)
    db.session.commit()
    return jsonify({'message': 'Candidate added', 'id': new_candidate.id}), 201

@app.route('/candidates/<int:id>', methods=['PUT'])
def update_candidate(id):
    data = request.get_json()
    candidate = Candidate.query.get(id)
    if candidate:
        candidate.name = data.get('name', candidate.name)
        candidate.email = data.get('email', candidate.email)
        candidate.resume = data.get('resume', candidate.resume)
        candidate.status = data.get('status', candidate.status)
        db.session.commit()
        return jsonify({'message': 'Candidate updated'})
    return jsonify({'message': 'Candidate not found'}), 404

@app.route('/candidates/<int:id>', methods=['DELETE'])
def delete_candidate(id):
    candidate = Candidate.query.get(id)
    if candidate:
        db.session.delete(candidate)
        db.session.commit()
        return jsonify({'message': 'Candidate deleted'})
    return jsonify({'message': 'Candidate not found'}), 404

# New route to handle job descriptions and scoring candidates
@app.route('/match', methods=['POST'])
def match_candidates():
    data = request.get_json()
    if 'job_description' not in data:
        return jsonify({'message': 'Job description is required'}), 400
    
    job_description = data['job_description']
    job_keywords = extract_keywords(job_description)

    candidates = Candidate.query.all()
    scored_candidates = []

    for candidate in candidates:
        resume_keywords = extract_keywords(candidate.resume)
        score = calculate_match_score(job_keywords, resume_keywords)
        scored_candidates.append({
            'id': candidate.id,
            'name': candidate.name,
            'email': candidate.email,
            'resume': candidate.resume,
            'score': score
        })
    
    # Sort candidates by score in descending order
    scored_candidates.sort(key=lambda x: x['score'], reverse=True)
    
    return jsonify(scored_candidates)

def extract_keywords(text):
    # Simple keyword extraction based on word frequency
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

def calculate_match_score(job_keywords, resume_keywords):
    # Simple matching score based on common keyword frequency
    score = 0
    for word, count in job_keywords.items():
        if word in resume_keywords:
            score += min(count, resume_keywords[word])
    return score

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
