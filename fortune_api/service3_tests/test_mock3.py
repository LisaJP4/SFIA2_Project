from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app
        
class TestHome(TestBase):
    def test_get_fortune(self):
        for _ in range(10):
            response = self.client.get(url_for('getfortune'))
            self.assertIn(response.data.decode('utf-8'), ["True", "False"])


        # for _ in range(50):
        #     response = self.client.get(url_for('get_day'))
        #     self.assertIn(response.data.decode('utf-8'), ["1", "2", "3", "4", "5", "6", "7"])
        #     self.assertEqual(response.status_code, 200)
