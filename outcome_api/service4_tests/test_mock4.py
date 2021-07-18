# from unittest import mock
from unittest.mock import patch
from flask import url_for, jsonify, request
from flask_testing import TestCase
import requests_mock
import requests
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app
        
class TestHome(TestBase):


   # # def test_get_day(self):
    # with patch('random.choice') as r:
    #         r.return_value = '2'
    #         response = self.client.get(url_for('get_day'))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertEqual(b'2', response.data)

