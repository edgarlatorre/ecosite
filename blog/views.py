from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from ecosite.blog.models import Post

def post_index(request):
	posts = Post.objects.order_by('-published')
	return render_to_response('blog/index.html', {'posts':posts}, context_instance = RequestContext(request))
	
def post_show(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render_to_response('blog/show.html', locals(), context_instance = RequestContext(request))
	
def show_posts_by_category(request, category_id):
	posts = Post.objects.filter(category__id=category_id)
	return render_to_response('blog/index.html', locals(), context_instance = RequestContext(request))




