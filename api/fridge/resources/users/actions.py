from flask import Blueprint, Response

from fridge.wrappers import JSONResponse
from fridge.middlewares.request import accepts, paginate

users_resource = Blueprint('users_resource', __name__)


@users_resource.route('/users', methods=['OPTIONS'])
def users_options():
    headers = [('Allow', 'GET')]
    return Response(status=200, headers=headers)


@users_resource.route('/users/<int:user_id>', methods=['OPTIONS'])
def user_options(user_id):
    headers = [('Allow', 'GET', 'POST', 'PUT', 'DELETE')]

    return Response(status=200, headers=headers)


@users_resource.route('/users', methods=['GET'])
@accepts(['application/json'])
@paginate
def list():
    """List Fridge server registered users"""
    return JSONResponse(status=200)


@users_resource.route('/users/<int:user_id>', methods=['GET'])
@accepts(['application/json'])
@paginate
def get(user_id):
    """Retrieve a Fridge server registered user"""
    return JSONResponse(status=200)


@users_resource.route('/users', methods=['POST'])
@accepts(['application/json'])
def create():
    """Create a Fridge server user and related accounts"""
    return JSONResponse(status=201)


@users_resource.route('/users', methods=['PUT'])
@accepts(['application/json'])
def update():
    """Update a Fridge server user account"""
    return JSONResponse(status=201)


@users_resource.route('/users/<int:user_id>', methods=['POST'])
@accepts(['application/json'])
def delete():
    """Delete a Fridge server user and it's credentials"""
    return JSONResponse(204)

