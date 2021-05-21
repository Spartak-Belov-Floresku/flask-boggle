from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
import simplejson as json

class FlaskTests(TestCase):


    '''Testing to load home page with game board'''
    def test_home_page(self):

        with app.test_client() as client:

            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Welcome to Boggle Game!</h1>', html)

    '''Test runs the POST request to check that the word exist'''
    def test_check_word(self):

        with app.test_client() as client:

            client.get('/')
            resp = client.post('/word', data=json.dumps(dict(word='apple')), content_type='application/json')

            html = resp.get_data(as_text=True)

            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('result', html)


    '''Test runs the POST request to increase total score of the user'''
    def test_user_score(self):

        with app.test_client() as client:

            client.get('/')
            resp = client.post('/score', data=json.dumps(dict(score='1')), content_type='application/json')

            html = resp.get_data(as_text=True)

            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('1', html)


    '''Test runs the GET request to get a hint word for the user'''
    def test_user_score(self):

        with app.test_client() as client:

            client.get('/')
            resp = client.get('/hint')

            html = resp.get_data(as_text=True)

            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('hint_word', html)
