from django.contrib import admin
from contact.models import ContactModel

class MyContactAdmin(admin.ModelAdmin):
    #date_hierarchy = 'created_on'
    list_display = ('name','address','city', 'state', 'zip', 'phone', 'subject', 'email',)
    #list_filter = ['is_accepted',]
    
admin.site.register(ContactModel, MyContactAdmin)
