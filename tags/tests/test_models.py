from django.test import TestCase
from ecosite.tags.models import Tag
class TagTest(TestCase) :
	def test_should_have_name_as_unicode(self):
		tag = Tag(name='tag')
		self.assertTrue(str(tag) == tag.name)