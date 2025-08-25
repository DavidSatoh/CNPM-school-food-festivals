from flask import Blueprint, request, jsonify
from services.food_service import FoodService
from infrastructure.repositories.food_repository import FoodRepository
from api.schemas.food import FoodRequestSchema, FoodResponseSchema
from infrastructure.databases.mssql import session

bp = Blueprint('food', __name__, url_prefix='/foods')

food_service = FoodService(FoodRepository(session))
request_schema = FoodRequestSchema()
response_schema = FoodResponseSchema()

@bp.route('/', methods=['GET'])
def list_foods():
    foods = food_service.list_foods()
    return jsonify(response_schema.dump(foods, many=True)), 200

@bp.route('/<int:food_id>', methods=['GET'])
def get_food(food_id):
    food = food_service.get_food(food_id)
    if not food:
        return jsonify({'message': 'Food not found'}), 404
    return jsonify(response_schema.dump(food)), 200

@bp.route('/', methods=['POST'])
def create_food():
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    food = food_service.create_food(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        category=data['category'],
        event_id=data['event_id']
    )
    return jsonify(response_schema.dump(food)), 201

@bp.route('/<int:food_id>', methods=['PUT'])
def update_food(food_id):
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    food = food_service.update_food(
        food_id=food_id,
        name=data['name'],
        description=data['description'],
        price=data['price'],
        category=data['category'],
        event_id=data['event_id']
    )
    if not food:
        return jsonify({'message': 'Food not found'}), 404
    return jsonify(response_schema.dump(food)), 200

@bp.route('/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    result = food_service.delete_food(food_id)
    if not result:
        return jsonify({'message': 'Food not found'}), 404
    return '', 204