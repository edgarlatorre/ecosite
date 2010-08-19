from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	author = models.ForeignKey('auth.User', blank = True, null = False)
	published = models.DateTimeField()

	class Admin :
		pass
	
	def __unicode__(self) :
		return self.title
