# coding: utf-8
from lettuce import step, world
from ecosite.blog.models import Post
from django.test.client import Client
from ludibrio import Mock

@step(u'que existem (\\d+) artigos publicados')
def save_posts(step, amount_of_posts) :
	world.posts = []
	for i in xrange(int(amount_of_posts)) :
		title = 'Post %d' % i
		post = Post(title=title)
		world.posts.append(post)
		
@step(u'vou para a página inicial')
def visit_index_page(step) :
	with Mock() as Post :
		Post.objects.all() << world.posts
	
	posts = Post.objects.all()	
	client = Client()
	response = client.get('/')

@step(u'eu deveria ver a listagem dos artigos')
def see_posts(step):
	"""docstring for see_posts"""
	pass