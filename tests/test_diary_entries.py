import unittest
from app import app


class DiaryEntryTestCase(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_all_entries(self):
        """Tests that all entries can be retrieved"""
        testing_user = app.test_client(self)
        response = testing_user.get("/api/v1/entries", content_type="application/json")
        assert b'Exhausted' in response.data


if __name__ == '__main__':
    unittest.main()
