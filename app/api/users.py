from flask import Blueprint

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/', methods=('GET',))
def get_all_users():
    """get all users"""
    return 'get all users', 200


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


