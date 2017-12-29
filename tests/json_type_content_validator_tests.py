import unittest
import json

from tests.dummy_flask_app import app

class JsonTypeContentValidatorTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_dummy_resource_should_return_data_given_json_content_header(self):
        # given
        url = '/echo-resource'
        data = dict(key='value')

        # when
        result = self.app.get(
            url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

        # then
        self.assertEqual(result.status_code, 200)
        result_data = json.loads(result.data)
        self.assertDictEqual(data, result_data)

    def test_dummy_resource_should_return_400_given_no_json_content_header(self):
         # given
        url = '/echo-resource'
        data = dict(key='value')

        # when
        result = self.app.get(url, data=json.dumps(data))

        # then
        self.assertEqual(result.status_code, 400)
        result_data = json.loads(result.data)
        expected_result = dict(
            error_code=1000,
            message='Missing Content-Type header application/json'
        )
        self.assertDictEqual(result_data, expected_result)
