from django.db import models
from datetime import datetime
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	author = models.ForeignKey('auth.User', blank=True, null = False)
	published = models.DateTimeField(default=datetime.now, blank=True)
	slug = models.SlugField(max_length=100, blank=True)

	class Admin :
		pass
	
	def get_absolute_url(self):
		return reverse('post-show', kwargs={'slug':self.slug})
	
	def __unicode__(self) :
		return self.title

def post_pre_save(signal, instance, sender, **kwargs):
	instance.slug = slugify(instance.title)
	
signals.pre_save.connect(post_pre_save, sender=Post)