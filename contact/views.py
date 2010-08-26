from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.core.mail import send_mail

class FormContact(forms.Form):
	name = forms.CharField(max_length=50)
	email = forms.EmailField(required=False)
	message = forms.Field(widget=forms.Textarea)
	
	def send(self):
		title = 'Mensagem enviada pelo ecofriend'
		to = 'osoturno@gmail.com'
		message = """
		Nome: %(name)s
		E-mail: %(email)s
		Mensagem:
		%(message)s
		""" % self.cleaned_data
		
		send_mail(subject=title, message=message, from_email=to, recipient_list=[to])
		

def contact(request):
	if request.method == 'POST' :
			form = FormContact(request.POST)
			
			if form.is_valid() :
				form.send()
				show = 'Mensagem enviada.'
	else :
		form = FormContact()
				
	return render_to_response('contact/contact.html', locals(), context_instance=RequestContext(request))
