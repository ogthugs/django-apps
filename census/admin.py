from django.contrib import admin
from census.models import PersonsModel

class MyCensusAdmin(admin.ModelAdmin):
    #date_hierarchy = 'created_on'
    list_display = ('sex', 'dob', 'hispanic', 'race',)
    #list_filter = ['is_accepted',]
    
admin.site.register(PersonsModel, MyCensusAdmin)
