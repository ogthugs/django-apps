from django.db import models
import datetime
'''
class Address(models.Model):
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zip = models.IntegerField(max_length=5)
	
	def __unicode__(self):
		return self.name


class House(models.Model):
	residents_number = models.IntegerField(max_length=2)
	aditional_guests = models.IntegerField(max_length=90)
	owned = models.CharField(max_length=90)
	phone = models.IntegerField(max_length=10)
	
	def __unicode__(self):
		return self.name
'''

class PersonsModel(models.Model):
	#address = models.ForeignKey(Address)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zip = models.IntegerField(max_length=5)	
	name = models.CharField(max_length=90)
	sex = models.CharField(max_length=90)
	dob = models.DateField()
	hispanic = models.BooleanField(default=False)
	race = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name
	
