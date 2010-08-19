from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django import forms
from models import Post
from ecosite.tags import aplicar_tags


class FormPost(forms.ModelForm) :
	class Meta:
		model = Post
		
	tags = forms.CharField(max_length=30, required=False)
	
	def __init__(self, *args, **kwargs) :
		super(FormPost, self).__init__(*args, **kwargs)

		if self.instance.id:
			self.initial['tags'] = tags_to_object(self.instance)
	
class AdminPost(ModelAdmin) :
	form = FormPost
	
	def save_model(self, request, obj, form, change) :
		super(AdminPost, self).save_model(request, obj, form, change)
		apply_tags(obj, form.cleaned_data['tags'])
		
admin.site.register(Post, AdminPost)