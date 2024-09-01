from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    resume = db.Column(db.Text, nullable=False)  # Changed to Text for larger resume content
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
    return jsonify({'message': 'Candidate added'}), 201

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Allows access from external devices if needed
