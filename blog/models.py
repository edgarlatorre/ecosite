from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	publish = models.DateTimeField()

	class Admin :
		pass
	
	def __unicode__(self) :
		return self.title
