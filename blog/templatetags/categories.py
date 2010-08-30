from django.template import Library, Node
from ecosite.blog.models import Category

register=Library()
def get_all_categories(parser, token) :
	"""
		{% get_categories %}
	"""
	return CategoryMenuObject()
	

class CategoryMenuObject(Node):
	def render(self, context):
		context['get_all_categories'] = Category.objects.all()
		return ''

register.tag('get_categories', get_all_categories)
