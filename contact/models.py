from django.db import models

class ContactModel(models.Model):

	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zip = models.IntegerField(max_length=5)
	phone = models.IntegerField(max_length=10)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField()
	
	def __unicode__(self):
		return self.name
	

