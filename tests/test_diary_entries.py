import unittest
from api.v1 import app
import json


class DiaryEntryTestCase(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.my_entries = [
            {
                'entry_id': 1,
                'entry_date': '18 June 2018',
                'entry_time': '22 15',
                'entry_title': 'Learning Flask',
                'content': 'Flask is a micro-framework based on python. '
                           'Flask is useful for designing APIs.'
            },
            {
                'entry_id': 2,
                'entry_date': '19 June 2018',
                'entry_time': '22 15',
                'entry_title': 'My first Flask API',
                'content': 'I am following some flask youtube videos from pretty printed. '
                           'I am going to work along with them then later create my own product.'
            }
        ]
    
    def test_get_all_entries(self):
        """Tests that all entries can be retrieved"""
        testing_user = app.test_client(self)
        response = testing_user.get("/api/v1/entries", content_type="application/json")
        assert b'Exhausted' in response.data
        assert b'Excitement' in response.data

    def test_get_specific_entry(self):
        testing_user = app.test_client(self)
        my_id = {"entry_id": 1}
        response = testing_user.get("/api/v1/entries/{}".format(my_id['entry_id']))
        assert b'Exhausted' in response.data

    def test_new_entry(self):
        """Tests that a new entry can be created"""
        new_entry = {
            'entry_id': 1,
            'entry_date': '7 June 2018',
            'entry_time': '18 15',
            'title': 'Exhausted',
            'content': 'Today am spent!'}
        testing_user = app.test_client(self)
        response = testing_user.post("/api/v1/entries", data=json.dumps(new_entry), content_type="application/json")
        assert response.status_code == 200

    def test_modify_entry(self):
        """Tests that a user can modify an entry"""
        my_entry = {
            'entry_id': 1,
            'entry_date': '7 June 2018',
            'entry_time': '18 15',
            'title': 'Exhausted',
            'content': 'Today am spent!'}
        testing_user = app.test_client(self)
        my_entry['title'] = 'Tired!'
        response = testing_user.put("/api/v1/entries/1", data=json.dumps(my_entry), content_type="application/json")
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
