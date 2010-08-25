from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms

class FormContact(forms.Form):
	name = forms.CharField(max_length=50)
	email = forms.EmailField(required=False)
	message = forms.Field(widget=forms.Textarea)
		

def contact(request):
	if request.method == 'POST' :
			form = FormContact(request.POST)
			
			if form.is_valid() :
				form.send()
				show = 'Mensagem enviada.'
	else :
		form = FormContact()
				
	return render_to_response('contact/contact.html', locals(), context_instance=RequestContext(request))
