from flask import Blueprint, jsonify, request

from app.models.users import Users

users_bp = Blueprint('users', __name__, url_prefix='/users')


def send_error_message(message, status_code):
    """send error message with the status code

    Parameters
    ----------
    status_code : int
    message : str
    """
    return jsonify({'message': message}), status_code


@users_bp.route('/', methods=('GET',))
def get_all_users():
    """get all users"""
    all_users = Users.query.all()

    if not all_users:
        return send_error_message('no users found', 404)

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
    req_json = request.get_json()

    if 'name' not in req_json:
        return send_error_message('missing "name" property in request', 400)

    name = req_json.get('name')

    new_user = Users(name=name)
    new_user.save()
    new_user.refresh_from_db()

    return jsonify({
        'name': new_user.name,
        'id': new_user.id,
    }), 200


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
