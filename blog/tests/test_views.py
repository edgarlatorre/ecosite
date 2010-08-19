from django.test import TestCase
from django.test import Client

class PostViewsTest(TestCase) :
	client = Client()
	
	def test_index(self) :
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'blog/index.html')
		self.assertTrue(response.status_code == 200)