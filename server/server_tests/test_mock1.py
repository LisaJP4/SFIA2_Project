# from unittest import mock
# from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app
        
class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as d:
            d.get('http://plague_days:5001/getday', text="4")
            d.get('http://plague_fortune:5003/getfortune', text="False")
            d.post('http://plague_outcome:5002/getoutcome', text="outcome")
            response = self.client.get(url_for('home'))
            self.assertIn(b'And your fate was as follows...', response.data)