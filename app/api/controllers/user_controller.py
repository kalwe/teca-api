from flask import jsonify, request
from app.core.services.user_service import UserService

class UserController:
    """
    Controller that handles user-related HTTP requests.
    """
    @staticmethod
    def create_user():
        data = request.get_json()
        user_service = UserService()
        user = user_service.create_user(data)
        return jsonify(user), 201

    @staticmethod
    def get_user(user_id):
        user_service = UserService()
        user = user_service.get_user(user_id)
        if user:
            return jsonify(user), 200
        return jsonify({"message": "User not found"}), 404
