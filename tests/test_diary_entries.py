"""This module the test_diary_entries module.

This module tests the entries endpoints of the API.
"""


import unittest
import json

from api import app
from api.v1.endpoints.users import my_users
from api.v1.endpoints.entries import my_entries


class DiaryEntryTestCase(unittest.TestCase):
    @staticmethod
    def create_app():
        app['TESTING'] = True
        return app

    def setUp(self):
        self.my_entries = [
            {
                'entry_date': '18 June 2018',
                'entry_time': '22 15',
                'title': 'Learning Flask',
                'content': 'Flask is a micro-framework based on python. Flask is useful for designing APIs.'
            },
            {
                'entry_date': '19 June 2018',
                'entry_time': '22 15',
                'title': 'My first Flask API',
                'content': 'I am following some flask youtube videos from pretty printed. I am going to work along with'
                           'them then later create my own product.'
            }]
        self.my_entry = [
            {
                'entry_id': 3,
                'entry_date': '20 June 2018',
                'title': 'Day Two Flask API',
                'content': 'So, pretty printed is very nice channel, they explain pretty well. '
                           'Yesterday, i created a simple todo list API using flask and SQLAlchemy'
            }
        ]

    def test_API_can_not_make_an_entry_with_missing_values(self):
        """Tests that the API will fail to create new entry if any value is blank"""
        testing_user = app.test_client(self)
        self.my_entries[0]['title'] = ''
        response = testing_user.post('/api/v1/entries', data=json.dumps(self.my_entries[0]),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Please fill in title', str(response.data))

    def test_API_can_not_make_an_entry_with_missing_key(self):
        """Tests that the API will fail  to create a new entry if a key is missing"""
        testing_user = app.test_client(self)
        response = testing_user.post('/api/v1/entries', data=json.dumps(self.my_entry[0]),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing entry_time', str(response.data))

    def test_API_can_make_new_entry(self):
        """Tests that a new entry can be created"""
        testing_user = app.test_client(self)
        # Add first entry
        response = testing_user.post('/api/v1/entries', data=json.dumps(self.my_entries[0]),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Your memory entitled ' + self.my_entries[0]['title'] + ' has been saved', str(response.data))
        # Add second entry
        res = testing_user.post('/api/v1/entries', data=json.dumps(self.my_entries[1]), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('Your memory entitled ' + self.my_entries[1]['title'] + ' has been saved', str(res.data))

    def test_get_all_entries(self):
        """Tests that all entries can be retrieved"""
        testing_user = app.test_client(self)
        # Add first entry
        res = testing_user.post('/api/v1/entries', data=json.dumps(self.my_entries[0]), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('Your memory entitled ' + self.my_entries[0]['title'] + ' has been saved', str(res.data))
        # Add second entry
        response = testing_user.post('/api/v1/entries', data=json.dumps(self.my_entries[1]),
                                     content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('Your memory entitled ' + self.my_entries[1]['title'] + ' has been saved', str(response.data))
        # Get all entries
        final_response = testing_user.get('/api/v1/entries')
        self.assertEqual(final_response.status_code, 200)
        self.assertIn('Learning Flask', str(final_response.data))
        self.assertIn('My first Flask API', str(final_response.data))

    def test_get_specific_entry(self):
        """Tests that user can get specific entry"""
        testing_user = app.test_client(self)
        # Add first entry
        res = testing_user.post('/api/v1/entries', data=json.dumps(self.my_entries[0]),
                                content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('Your memory entitled ' + self.my_entries[0]['title'] + ' has been saved', str(res.data))
        # Get specific entry
        my_id = {'entry_id': 1}
        response = testing_user.get('/api/v1/entries/{}'.format(my_id['entry_id']))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Learning Flask', str(response.data))

    def test_API_will_fail_to_update_when_content_is_empty(self):
        """Tests that an update will fail if content provided is an emtpy string"""
        testing_user = app.test_client(self)
        self.my_entries[0]['content'] = ''
        response = testing_user.put('/api/v1/entries/1', data=json.dumps(self.my_entries[0]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Please provide content', str(response.data))

    def test_API_will_fail_to_update_when_title_is_empty(self):
        """Tests that an update will fail if title provided is an emtpy string"""
        testing_user = app.test_client(self)
        self.my_entries[1]['title'] = ''
        response = testing_user.put('/api/v1/entries/1', data=json.dumps(self.my_entries[1]),
                                    content_type='application/json')
        self.assertIn('Please provide title', str(response.data))

    def test_modify_entry(self):
        """Tests that a user can modify an entry"""
        testing_user = app.test_client(self)
        res = testing_user.post('/api/v1/entries', data=json.dumps(self.my_entries[0]),
                                content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('Your memory entitled ' + self.my_entries[0]['title'] + ' has been saved', str(res.data))
        self.my_entries[0]['title'] = 'Learnt Flask!'
        response = testing_user.put('/api/v1/entries/1', data=json.dumps(self.my_entries[0]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Entry updated', str(response.data))


if __name__ == '__main__':
    unittest.main()
