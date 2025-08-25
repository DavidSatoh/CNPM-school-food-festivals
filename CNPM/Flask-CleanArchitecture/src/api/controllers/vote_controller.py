from flask import Blueprint, request, jsonify
from src.infrastructure.repositories.vote_repository import VoteRepository
from src.services.vote_service import VoteService

vote_bp = Blueprint('vote', __name__)
vote_service = VoteService(VoteRepository())

@vote_bp.route('/votes', methods=['POST'])
def create_vote():
    data = request.get_json()
    try:
        vote = vote_service.create_vote(
            user_id=data['user_id'],
            food_id=data['food_id'],
            event_id=data['event_id'],
            score=data['score']
        )
        return jsonify({'message': 'Vote created', 'vote': vote.__dict__}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@vote_bp.route('/votes/<int:vote_id>', methods=['GET'])
def get_vote(vote_id):
    vote = vote_service.get_vote(vote_id)
    if vote:
        return jsonify(vote.__dict__)
    return jsonify({'error': 'Vote not found'}), 404

@vote_bp.route('/votes/food/<int:food_id>', methods=['GET'])
def get_votes_by_food(food_id):
    votes = vote_service.get_votes_by_food(food_id)
    return jsonify([vote.__dict__ for vote in votes])

@vote_bp.route('/votes/event/<int:event_id>', methods=['GET'])
def get_votes_by_event(event_id):
    votes = vote_service.get_votes_by_event(event_id)
    return jsonify([vote.__dict__ for vote in votes])

@vote_bp.route('/votes/<int:vote_id>', methods=['DELETE'])
def delete_vote(vote_id):
    vote_service.delete_vote(vote_id)
    return jsonify({'message': 'Vote deleted'})
