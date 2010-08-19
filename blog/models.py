from django.db import models
from datetime import datetime
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	author = models.ForeignKey('auth.User', null = False)
	published = models.DateTimeField(default=datetime.now, blank=True)
	slug = models.SlugField(max_length=100, blank=True, unique=True)

	class Admin :
		pass
	
	def get_absolute_url(self):
		return reverse('post-show', kwargs={'slug':self.slug})
	
	def __unicode__(self) :
		return self.title

def post_pre_save(signal, instance, sender, **kwargs):
	if not instance.slug :
		slug = slugify(instance.title)
		new_slug = slug
		count = 0;
		
		while Post.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0 :
			count += 1
			new_slug = '%s-%d' % (slug, count)
			
		instance.slug = new_slug
	
signals.pre_save.connect(post_pre_save, sender=Post)