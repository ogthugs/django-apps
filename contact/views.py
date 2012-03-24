from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from django.contrib import messages

#import forms
from contact.forms import ContactForm

#import models
from contact.models import ContactModel

def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))

def received(request):
	return render_to_response('contact/received.html', context_instance=RequestContext(request))

def my_contact(request): #ref from URL's
    if request.method == 'POST':
        form = ContactForm(request.POST)#reference forms.py
        if form.is_valid():
            my_contacts = ContactModel()#reference models.py
            my_contacts.name = form.cleaned_data['name']
            my_contacts.address = form.cleaned_data['address']
            my_contacts.city = form.cleaned_data['city']
            my_contacts.state = form.cleaned_data['state']
            my_contacts.zip = form.cleaned_data['zip']
            my_contacts.phone = form.cleaned_data['phone']
            my_contacts.email = form.cleaned_data['email']
            my_contacts.subject = form.cleaned_data['subject']
            my_contacts.message = form.cleaned_data['message']
            my_contacts.save()
            return redirect('received')
    else:
        form = ContactForm() #unbound form
    return render_to_response('contact/wtfcontacts.html',{'form':form}, context_instance=RequestContext(request)) #need to fill in URL