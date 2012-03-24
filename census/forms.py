from django import forms
from census.models import PersonsModel
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget

from django.contrib.localflavor.us.forms import USPhoneNumberField, USStateSelect, USZipCodeField

BIRTH_YEAR_CHOICES = (range(1900,2012))
GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'))
HOUSE2_CHOICES = (('Y', 'YES'),('N','NO'))
RACE = (('blue', 'Blue'),
                            ('green', 'Green'),
                            ('black', 'Black'))

'''class Address(forms.Form):
	address = forms.CharField(max_length=200)
	city = forms.CharField(max_length=100)
	state = forms.CharField(max_length=100)
	zip = forms.IntegerField()
'''
	
class PersonsForm(forms.Form):
	#address = forms.ForeignKey(Address)
	address = forms.CharField(max_length=200)
	city = forms.CharField(max_length=100)
	state = forms.CharField(widget=USStateSelect)
	zip = forms.CharField(USZipCodeField)
	name = forms.CharField(max_length=90)
	sex = ChoiceField(widget=RadioSelect, choices=GENDER_CHOICES)
	dob = DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	hispanic = forms.BooleanField(required=False)
	race = ChoiceField(widget=RadioSelect, choices=RACE)