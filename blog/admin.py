from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django import forms
from django.conf import settings
from models import Post
from ecosite.tags import apply_tags, tags_to_object


class FormPost(forms.ModelForm) :
	class Media:
		js = ('%s/js/tiny_mce/tiny_mce.js' % settings.MEDIA_URL, '%s/js/textareas.js' % settings.MEDIA_URL)
    
	class Meta:
		model = Post
		
	tags = forms.CharField(max_length=30, required=False)
	
	def __init__(self, *args, **kwargs) :
		super(FormPost, self).__init__(*args, **kwargs)

		if self.instance.id:
			self.initial['tags'] = tags_to_object(self.instance)
	
class AdminPost(ModelAdmin) :
	class Media:
		js = ('%s/js/tiny_mce/tiny_mce.js' % settings.MEDIA_URL, '%s/js/textareas.js' % settings.MEDIA_URL)
		
	form = FormPost	
	def save_model(self, request, obj, form, change) :
		super(AdminPost, self).save_model(request, obj, form, change)
		apply_tags(obj, form.cleaned_data['tags'])
		
class CustomFlatPageAdmin(FlatPageAdmin):
	class Media:
		js = ('%s/js/tiny_mce/tiny_mce.js' % settings.MEDIA_URL, '%s/js/textareas.js' % settings.MEDIA_URL)

admin.site.register(Post, AdminPost)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)