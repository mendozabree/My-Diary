"""
This is the users module

This module is the view for the API regarding users
"""

from flask import jsonify, request, make_response

from api import app
from api.v1.my_classes import User

my_users = []
first_user = User()


@app.route('/', methods=['GET'])
def home():
    return jsonify({'Message': 'You are welcome'})


@app.route('/api/v1/users', methods=['POST'])
def signup():
    signup_data = request.get_json()
    message = first_user.signup(signup_data=signup_data, my_users=my_users)
    return make_response(jsonify({'Message': message['message']})), message['code']


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    login_data = request.get_json()
    message = User.login(login_data=login_data, my_users=my_users)
    return make_response(jsonify({'Message': message['message']})), message['code']
