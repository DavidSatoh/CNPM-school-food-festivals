import jwt
from flask import Blueprint, request, jsonify, current_app
from datetime import datetime, timedelta
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
auth_service = AuthService()

def generate_token(user):
    payload = {
        'user_id': user.id,
        'role': user.role,
        'exp': datetime.now(timezone.utc) + timedelta(hours=2)
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = auth_service.login(data['user_name'], data['password'])
    if not user:
        return jsonify({'error': 'Invalid credentials'}), 401
    token = generate_token(user)
    return jsonify({'token': token, 'role': user.role})

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    role = data.get('role', 'user')
    user = auth_service.register(data['user_name'], data['password'], role)
    if not user:
        return jsonify({'error': 'User already exists'}), 400
    return jsonify({'message': 'Register successful', 'user_id': user.id, 'role': user.role}), 201