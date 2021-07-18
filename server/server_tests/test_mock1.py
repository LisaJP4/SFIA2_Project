# from unittest import mock
# from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app
        
# class TestHome(TestBase):
#     def test_home(self):
#         with requests_mock.Mocker() as d:
#             d.get('http://plague_days:5001/getday', text='4')
#             d.get('http://plague_fortune:5003/getfortune', text='False')
#             d.post('http://plague_outcome:5002/getoutcome', json={'4', 'False'})
#             response = self.client.get(url_for('home'))
#             self.assertEqual(response.status_code, 200)
#             self.assertIn(b'You had it for 4 days', response.data)
#             self.assertIn(b'Your fortune has turned out to be... Unlucky!', response.data)
#             self.assertIn(b'The plague turns your skin blue. You survive, but spend the rest of your life as a pariah.', response.data)
