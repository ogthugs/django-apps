from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from django.contrib import messages



#import forms
from census.forms import PersonsForm

#import models
from census.models import PersonsModel

def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))

def received(request):
	return render_to_response('census/received.html', context_instance=RequestContext(request))

def my_census(request): #ref from URL's
    if request.method == 'POST':
        form = PersonsForm(request.POST)#reference forms.py
        if form.is_valid():
            my_census = PersonsModel()#reference models.py
            my_census.address = form.cleaned_data['address']
            my_census.city = form.cleaned_data['city']
            my_census.state = form.cleaned_data['state']
            my_census.zip = form.cleaned_data['zip']
            my_census.name = form.cleaned_data['name']
            my_census.sex = form.cleaned_data['sex']
            my_census.dob = form.cleaned_data['dob']
            my_census.hispanic = form.cleaned_data['hispanic']
            my_census.race = form.cleaned_data['race']
            my_census.save()
            return redirect('received')
    else:
        form = PersonsForm() #unbound form
    return render_to_response('census/wtfcensus.html',{'form':form}, context_instance=RequestContext(request)) #need to fill in URL