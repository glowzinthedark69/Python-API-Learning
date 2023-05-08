from flask import Flask, request, jsonify

app = Flask(__name__)

users = []


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['userId'] == user_id:
            return jsonify(user)
    return jsonify({'message': 'User not found'}), 404


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data['userId']
    # check if user with the same user_id already exists
    for user in users:
        if user['userId'] == int(user_id):
            return jsonify({'Error message': 'This user already exists. Please verify information.'}), 400
    # create new user
    user = {
        'name': data['name'],
        'userId': user_id,
        'city': data['city'],
        'country': data['country'],
        'jobTitle': data['jobTitle']
    }
    users.append(user)
    return jsonify(user), 201


@app.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    data = request.get_json()
    if data['userId'] != user_id:
        return jsonify({'message': 'User ID in request body does not match URL parameter'}), 400
    for user in users:
        if user['userId'] == user_id:
            if 'name' in data:
                user['name'] = data['name']
            if 'city' in data:
                user['city'] = data['city']
            if 'country' in data:
                user['country'] = data['country']
            if 'jobTitle' in data:
                user['jobTitle'] = data['jobTitle']
            return jsonify(user)
    return jsonify({'message': 'User not found'}), 404


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user['userId'] == user_id:
            user['name'] = data['name']
            user['city'] = data['city']
            user['country'] = data['country']
            user['jobTitle'] = data['jobTitle']
            return jsonify(user)
    return jsonify({'message': 'User not found'}), 404


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['userId'] == user_id:
            users.remove(user)
            return jsonify({'message': 'User has been successfully deleted.'})
    return jsonify({'message': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
