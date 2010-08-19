from django.db import models
from datetime import datetime

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	author = models.ForeignKey('auth.User', null = False)
	published = models.DateTimeField(default=datetime.now, blank=True)

	class Admin :
		pass
	
	def get_absolute_url(self):
		return 'post/%d' % self.id
	
	def __unicode__(self) :
		return self.title
