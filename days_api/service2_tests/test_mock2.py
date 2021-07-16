# from unittest import mock
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app
        
class TestHome(TestBase):
    def test_get_day(self):
        for _ in range(50):
            response = self.client.get(url_for('get_day'))
            self.assertIn(response.data.decode('utf-8'), ["1", "2", "3", "4", "5", "6", "7"])
            self.assertEqual(response.status_code, 200)

   # # def test_get_day(self):
    # with patch('random.choice') as r:
    #         r.return_value = '2'
    #         response = self.client.get(url_for('get_day'))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertEqual(b'2', response.data)

