from django.db import models

class Tag(models.Model):
	name = models.CharField(max_length=30, unique=True)
	
	def __unicode__(self):
		return self.name
		
