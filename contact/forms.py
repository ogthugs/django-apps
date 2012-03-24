from django import forms

from contact.models import ContactModel

class ContactForm(forms.Form):
    name = forms.CharField() 
    address = forms.CharField() 
    city = forms.CharField() 
    state = forms.CharField() 
    zip = forms.IntegerField() 
    phone = forms.IntegerField()
    email = forms.EmailField() 
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

