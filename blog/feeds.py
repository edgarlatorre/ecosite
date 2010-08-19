# coding: utf-8
from django.contrib.syndication.feeds import Feed
from models import Post

class LatestPosts(Feed) :
	title = 'Últimos artigos'
	link = '/'
	
	def items(self) :
		return Post.objects.all()