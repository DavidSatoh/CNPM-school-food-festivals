from flask import Blueprint, request, jsonify
from services.class_service import ClassService
from domain.models.classes import Classes
from infrastructure.repositories.class_repository import ClassRepository
from api.schemas.class_schema import ClassCreateSchema, ClassUpdateSchema, ClassResponseSchema
class_controller = Blueprint('class_controller', __name__)

# You need to inject the actual repository instance when initializing ClassService
class_service = ClassService(repository=ClassRepository())  # Replace with actual implementation

create_class_schema = ClassCreateSchema()
update_class_schema = ClassUpdateSchema()
class_response_schema = ClassResponseSchema()

@class_controller.route('/classes', methods=['GET'])
def get_all_classes():
    """
    ---
    get:
      summary: Get all classes
      responses:
        200:
          description: A list of all classes.
          schema: ClassResponseSchema
    """
    classes = class_service.get_all_classes()
    return jsonify([class_response_schema.dump(cls) for cls in classes])

@class_controller.route('/classes/<int:class_id>', methods=['GET'])
def get_class_by_id(class_id):
    """
    ---
    get:
      summary: Get a class by ID
      parameters:
        - name: class_id
          in: path
          required: true
          description: The ID of the class to retrieve.
          schema:
            type: integer
      responses:
        200:
          description: The class with the specified ID.
          schema: ClassResponseSchema
        404:
          description: Class not found.
    """
    cls = class_service.get_class_by_id(class_id)
    if cls:
        return jsonify(class_response_schema.dump(cls))
    return jsonify({'error': 'Class not found'}), 404

@class_controller.route('/classes', methods=['POST'])
def create_class():
    """
    ---
    post:
      summary: Create a new class
      requestBody:
        required: true
        content:
          application/json:
            schema: ClassCreateSchema
      responses:
        201:
          description: The created class.
          schema: ClassResponseSchema
    """
    data = request.get_json()
    class_data = Classes(id=0,**data)
    new_class = class_service.create_class(class_data)
    return jsonify(class_response_schema.dump(new_class)), 201

@class_controller.route('/classes/<int:class_id>', methods=['PUT'])
def update_class(class_id):
    """
    ---
    put:
      summary: Update a class by ID
      requestBody:
        required: true
        content:
          application/json:
            schema: ClassUpdateSchema
      responses:
        200:
          description: The updated class.
          schema: ClassResponseSchema
        404:
          description: Class not found.
    """
    data = request.get_json()
    class_data = Classes(id=class_id, **data)
    updated_class = class_service.update_class(class_id, class_data)
    if updated_class:
        return jsonify(updated_class.__dict__)
    return jsonify({'error': 'Class not found'}), 404

@class_controller.route('/classes/<int:class_id>', methods=['DELETE'])
def delete_class(class_id):
    """
    ---
    delete:
      summary: Delete a class by ID
      responses:
        204:
          description: Class deleted successfully.
        404:
          description: Class not found.
    """
    success = class_service.delete_class(class_id)
    if success:
        return jsonify({'message': 'Class deleted'})
    return jsonify({'error': 'Class not found'}), 404
