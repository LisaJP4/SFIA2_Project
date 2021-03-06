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
        for _ in range(4):
            response = self.client.get(url_for('getfortune'))
            self.assertIn(response.data.decode('utf-8'), ["True", "False"])