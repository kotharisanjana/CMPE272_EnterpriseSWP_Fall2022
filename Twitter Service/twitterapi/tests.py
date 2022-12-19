## Author: Ravi Teja Reddy

from django.test import TestCase
from django.test import Client
from django.test.client import RequestFactory
from django.urls import reverse
from . import views


# Create your tests here.

class TwitterViewTests(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    
    def test_tweet_creation(self):
        # Issue a POST request.
        response = self.client.post('create_tweet/', {'content': 'Hello, world new tweet324!'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        
        
    def test_get_timeline_tweets(self):
        # Issue a POST request.
        response = self.client.post('get_timeline_tweets/', {'content': 'SanjanaRajeshK1'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        
    def test_delete_tweet(self):
        # Issue a POST request.
        response = self.client.post('delete_tweet/', {'content': '1570987483512573955'})

        # Check that the response is 200 OK.              
        self.assertEqual(response.status_code, 200)