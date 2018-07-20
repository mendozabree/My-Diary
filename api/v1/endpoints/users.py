"""
This is the users module

This module is the view for the API regarding users
"""

from flask import jsonify, request

from app import app
from api.v1.my_classes import User

my_users = []
first_user = User()


@app.route('/api/v1/users', methods=['POST'])
def signup():
    signup_data = request.get_json()
    message = first_user.signup(signup_data=signup_data, my_users=my_users)
    return jsonify({'Message': message})


@app.route('/api/v1/auth/users', methods=['POST'])
def login():
    login_data = request.get_json()
    message = User.login(login_data=login_data, my_users=my_users)
    return jsonify({'Message': message})
