from src.api.controllers.todo_controller import bp as todo_bp
from src.api.controllers.food_controller import bp as food_bp


def register_routes(app):
    app.register_blueprint(todo_bp)
    app.register_blueprint(food_bp)
    