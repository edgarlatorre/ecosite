from django.test import TestCase
from ecosite.blog.models import Post

class PostTest(TestCase) :
	def test_should_have_a_title(self):
		post = Post()	
		self.assertFalse(self.post_is_valid(post))
		
	def test_should_have_a_body(self):
		post = Post(title='title')
		self.assertFalse(self.post_is_valid(post))
		
	def test_should_have_title_as_unicode(self) :
		post = Post(title="test", body="body")
		self.assertTrue(post.title == str(post))
		
	def test_published_is_not_obligatory(self):
		post = Post(title='test', body='body')
		self.assertFalse(self.post_is_valid(post))
		
	
	def post_is_valid(self, post):
		is_valid = True
		try :
			post.save()
		except :
			is_valid = False
		