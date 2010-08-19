from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from ecosite.blog.models import Post

def post_index(request):
	posts = Post.objects.order_by('-published')
	return render_to_response('blog/index.html', {'posts':posts}, context_instance = RequestContext(request))




