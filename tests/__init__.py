import unittest

from tests.dummy_flask_app import app

class JsonTypeContentValidatorTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_dummy_resource_should_return_data_given_json_content_header(self):
        pass

    def test_dummy_resource_should_return_400_given_no_json_content_header(self):
        pass
