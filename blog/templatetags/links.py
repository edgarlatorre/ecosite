from django.template import Library, Node
from ecosite.blog.models import Link

register=Library()
def get_links(parser, token):
	return LinkMenuObject()
	
class LinkMenuObject(Node):
	def render(self, context):
		context['get_all_links'] = Link.objects.all()
		return ''
		
register.tag('get_links', get_links)