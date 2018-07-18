import unittest
from api.v1 import app
import json


class DiaryEntryTestCase(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_all_entries(self):
        """Tests that all entries can be retrieved"""
        testing_user = app.test_client(self)
        response = testing_user.get("/api/v1/entries", content_type="application/json")
        assert b'Exhausted' in response.data
        assert b'Excitement' in response.data

    def test_modify_entry(self):
        """Tests that a user can modify an entry"""
        my_entry = {
            'entry_id': 1,
            'entry_date': '7 June 2018',
            'entry_time': '18 15',
            'title': 'Exhausted',
            'content': 'Today am spent!'
        }
        testing_user = app.test_client(self)
        my_entry['title'] = 'Tired!'
        response = testing_user.put("/api/v1/entries/1", data=json.dumps(my_entry), content_type="application/json")
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
