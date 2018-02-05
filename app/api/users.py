from flask import Blueprint, jsonify

from app.models.users import Users

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/', methods=('GET',))
def get_all_users():
    """get all users"""
    all_users = Users.query.all()

    if not all_users:
        return jsonify({'message': 'no users found'}), 404

    response = [
        {
            'id': user.id,
            'name': user.name,
        } for user in all_users
    ]
    return jsonify(response), 200


@users_bp.route('/', methods=('POST',))
def add_new_user():
    """add new user"""
    return 'get all users', 200


@users_bp.route('/<user_id>', methods=('GET',))
def get_single_user(user_id):
    """add new user"""
    return 'get single user', 200


@users_bp.route('/<user_id>', methods=('PATCH',))
def update_single_user(user_id):
    """add new user"""
    return 'update', 200


@users_bp.route('/<user_id>', methods=('DELETE',))
def delete_single_user(user_id):
    """add new user"""
    return 'delete', 200
