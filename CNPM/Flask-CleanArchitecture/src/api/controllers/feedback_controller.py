from flask import Blueprint, request, jsonify
from src.infrastructure.repositories.feedback_repository import FeedbackRepository
from src.services.feedback_service import FeedbackService

feedback_bp = Blueprint('feedback', __name__)
feedback_service = FeedbackService(FeedbackRepository())

@feedback_bp.route('/feedbacks', methods=['POST'])
def create_feedback():
    data = request.get_json()
    try:
        feedback = feedback_service.create_feedback(
            user_id=data['user_id'],
            content=data['content'],
            event_id=data.get('event_id'),
            food_id=data.get('food_id')
        )
        return jsonify({'message': 'Feedback created', 'feedback': feedback.__dict__}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@feedback_bp.route('/feedbacks/<int:feedback_id>', methods=['GET'])
def get_feedback(feedback_id):
    feedback = feedback_service.get_feedback(feedback_id)
    if feedback:
        return jsonify(feedback.__dict__)
    return jsonify({'error': 'Feedback not found'}), 404

@feedback_bp.route('/feedbacks/food/<int:food_id>', methods=['GET'])
def get_feedbacks_by_food(food_id):
    feedbacks = feedback_service.get_feedbacks_by_food(food_id)
    return jsonify([fb.__dict__ for fb in feedbacks])

@feedback_bp.route('/feedbacks/event/<int:event_id>', methods=['GET'])
def get_feedbacks_by_event(event_id):
    feedbacks = feedback_service.get_feedbacks_by_event(event_id)
    return jsonify([fb.__dict__ for fb in feedbacks])

@feedback_bp.route('/feedbacks/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    feedback_service.delete_feedback(feedback_id)
    return jsonify({'message': 'Feedback deleted'})
