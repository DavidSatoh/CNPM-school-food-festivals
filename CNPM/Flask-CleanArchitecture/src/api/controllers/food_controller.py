from flask import Blueprint, request, jsonify
from services.food_service import FoodService
from infrastructure.repositories.food_repository import FoodRepository
from api.schemas.food import FoodRequestSchema, FoodResponseSchema, FoodCreateSchema, FoodUpdateSchema
from infrastructure.databases.mssql import session
from domain.models.food import Food
bp = Blueprint('food', __name__, url_prefix='/foods')

food_service = FoodService(FoodRepository(session))
request_schema = FoodRequestSchema()
response_schema = FoodResponseSchema()
create_schema = FoodCreateSchema()
update_schema = FoodUpdateSchema()

@bp.route('/', methods=['GET'])
def list_foods():
        '''
        ---
        get:
            summary: Get all foods
            description: Returns a list of all foods
            responses:
                200:
                    description: A list of foods
                    content:
                        application/json:
                            schema:
                                type: array
                                items: FoodResponseSchema
        '''
        foods = food_service.list_foods()
        return jsonify(response_schema.dump(foods, many=True)), 200

@bp.route('/<int:food_id>', methods=['GET'])
def get_food(food_id):
        '''
        ---
        get:
            summary: Get a food by ID
            description: Returns a single food item
            parameters:
                - name: food_id
                  in: path
                  required: true
                  schema:
                    type: integer
                  description: ID của food cần lấy
            responses:
                200:
                    description: A food item
                    content:
                        application/json:
                            schema: FoodResponseSchema
                404:
                    description: Food not found
        '''
        food = food_service.get_food(food_id)
        if not food:
                return jsonify({'message': 'Food not found'}), 404
        return jsonify(response_schema.dump(food)), 200

@bp.route('/', methods=['POST'])
def create_food():
        '''
        ---
        post:
            summary: Create a new food
            description: Creates a new food item
            requestBody:
                required: true
                content:
                    application/json:
                        schema: FoodCreateSchema
            responses:
                201:
                    description: Food created
                    content:
                        application/json:
                            schema: FoodResponseSchema
                400:
                    description: Validation error
        '''
        data = request.get_json()
        errors = create_schema.validate(data)
        if errors:
                return jsonify(errors), 400
        food = food_service.create_food(
                Food(
                        id = 0,
                        name=data['name'],
                        gian_hang_id=data['gian_hang_id'],
                        price=data['price']
                )
        )
        return jsonify(response_schema.dump(food)), 201

@bp.route('/<int:food_id>', methods=['PUT'])
def update_food(food_id):
        '''
        ---
        put:
            summary: Update a food
            description: Updates an existing food item
            parameters:
                - name: food_id
                  in: path
                  required: true
                  schema:
                    type: integer
                  description: ID của food cần lấy
            requestBody:
                required: true
                content:
                    application/json:
                        schema: FoodUpdateSchema
            responses:
                200:
                    description: Food updated
                    content:
                        application/json:
                            schema: FoodResponseSchema
                400:
                    description: Validation error
                404:
                    description: Food not found
        '''
        data = request.get_json()
        errors = update_schema.validate(data)
        if errors:
                return jsonify(errors), 400
        food = food_service.update_food(
                food_id=food_id,
                food_data=Food(
                        name=data['name'],
                        price=data['price']
                )
        )
        if not food:
                return jsonify({'message': 'Food not found'}), 404
        return jsonify(response_schema.dump(food)), 200

@bp.route('/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
        '''
        ---
        delete:
            summary: Delete a food
            description: Deletes a food item by ID
            parameters:
                - name: food_id
                  in: path
                  required: true
                  schema:
                    type: integer
                  description: ID của food cần lấy
            responses:
                204:
                    description: Food deleted
                404:
                    description: Food not found
        '''
        result = food_service.delete_food(food_id)
        if not result:
                return jsonify({'message': 'Food not found'}), 404
        return '', 204