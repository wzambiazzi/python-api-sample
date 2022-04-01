from flask import Blueprint, jsonify, request

user_route = Blueprint('user', __name__, url_prefix='/user')


@user_route.route('/list', methods=['GET'])
def list_user():
    user_list = [{'id': 1, 'name': 'Wellington Zambiazzi'},
                 {'id': 2, 'name': 'João da Silva'}]
    return jsonify(user_list), 200


@user_route.route('/create', methods=['POST'])
def create_user():
    user = request.json
    return jsonify(user), 201


@user_route.route('/update/<id>', methods=['PUT'])
def update_user(id):
    user = request.json
    user['id'] = id
    return jsonify(user), 201


@user_route.route('/find', methods=['GET'])
def find_user():
    name = request.args.get('name')
    return jsonify('filtro=' + name), 200


@user_route.route('/<id>', methods=['DELETE'])
def delete_user(id):
    return jsonify({'message': 'User removed' + id}), 200
