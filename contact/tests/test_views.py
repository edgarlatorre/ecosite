from django.test import TestCase
from django.test import Client

class ContactViewTest(TestCase):
	def test_contact_template(self) :
		response = self.client.get('/contato/')
		self.assertTemplateUsed(response, 'contact/contact.html')
		self.assertTrue(response.status_code == 200)