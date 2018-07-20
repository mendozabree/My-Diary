import unittest
import json

from api.v1 import app
from api.v1.endpoints.users import my_users


class UserTestCase(unittest.TestCase):
    @staticmethod
    def create_app():
        app['TESTING'] = True
        return app

    def setUp(self):
        self.my_users = [
            {
                'first_name': 'Shem',
                'last_name': 'Nambale',
                'username': 'NShemus',
                'email': 'shem@gmail.com',
                'password': 'SNambale'
            },
            {
                'first_name': 'Jocy',
                'last_name': 'Pan',
                'username': 'JoPan',
                'email': 'jopan@gmail.com',
                'password': 'PanJoc'
            }
        ]
        self.my_user = [
            {
                'first_name': 'Shem',
                'last_name': 'Nambale',
                'email': 'shem@gmail.com',
                'password': 'SNambale'
            }
        ]
    def tearDown(self):
        my_users.clear()

    def test_API_can_not_sign_up_user_with_missing_key(self):
        testing_user = app.test_client(self)
        response = testing_user.post('/api/v1/users', data=json.dumps(self.my_user[0]),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Missing username', str(response.data))

    def test_API_can_not_sign_up_user_with_missing_value(self):
        testing_user = app.test_client(self)
        self.my_users[1]['first_name'] = ''
        response = testing_user.post('/api/v1/users', data=json.dumps(self.my_users[1]),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Please fill in first_name', str(response.data))

    def test_user_can_signup(self):
        testing_user = app.test_client(self)
        response = testing_user.post('/api/v1/users', data=json.dumps(self.my_users[0]),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome ' + self.my_users[0]['username'], str(response.data))
        res = testing_user.post('/api/v1/users', data=json.dumps(self.my_users[1]),
                                content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Welcome ' + self.my_users[1]['username'], str(res.data))

    def test_API_can_login_user(self):
        testing_user = app.test_client(self)
        response = testing_user.post('/api/v1/users', data=json.dumps(self.my_users[0]),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome ' + self.my_users[0]['username'], str(response.data))
        res = testing_user.post('/api/v1/users', data=json.dumps(self.my_users[1]),
                                content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Welcome ' + self.my_users[1]['username'], str(res.data))
        final_response = testing_user.post('/api/v1/auth/users', data=json.dumps(self.my_users[0]),
                                           content_type='application/json')
        self.assertEqual(final_response.status_code, 200)
        self.assertIn('Welcome back, ' + self.my_users[0]['username'], str(final_response.data))
        final_res = testing_user.post('/api/v1/auth/users', data=json.dumps(self.my_users[1]),
                                      content_type='application/json')
        self.assertEqual(final_res.status_code, 200)
        self.assertIn('Welcome back, ' + self.my_users[1]['username'], str(final_res.data))
