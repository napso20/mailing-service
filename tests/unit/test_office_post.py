import unittest
from flask import jsonify
from unittest.mock import MagicMock
from svc.models import PostOffice
from api import register_post_office

class RegisterPostOfficeTestCase(unittest.TestCase):
    def setUp(self):
        self.post_office_dao = MagicMock()
        self.data = {
            'address': '123 Main St',
            'zip_code': '12345',
            'name': 'Test Post Office'
        }

    def test_register_post_office_success(self):
        self.post_office_dao.create.return_value = None

        request = MagicMock()
        request.get_json.return_value = self.data

        response = register_post_office(request, self.post_office_dao)

        self.post_office_dao.create.assert_called_once_with(PostOffice(**self.data))

        expected_response = jsonify(message='Post office registered successfully'), 200
        self.assertEqual(response, expected_response)

    def test_register_post_office_failure(self):
        self.post_office_dao.create.side_effect = Exception('Test error')

        request = MagicMock()
        request.get_json.return_value = self.data

        response = register_post_office(request, self.post_office_dao)

        self.post_office_dao.create.assert_called_once_with(PostOffice(**self.data))

        expected_response = jsonify(message='Error registering post office', error='Test error'), 500
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
