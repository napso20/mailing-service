import unittest
from flask_testing import TestCase
from api import app

class APITestCase(TestCase):
    def create_app(self):
        return app

    def test_register_post_office(self):
        post_data = {
            "address": "123 Main St",
            "zip_code": "12345",
            "name": "Test Post Office"
        }
        response = self.client.post('/api/postoffice', json=post_data)
        self.assert200(response)
        self.assertIn(b"Post office registered successfully", response.data)

    def test_get_post_office(self):
        response = self.client.get('/api/postoffice/1')
        self.assert200(response)
        self.assertIn(b"Post office details", response.data)


if __name__ == '__main__':
    unittest.main()
