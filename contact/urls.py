from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^wtfcontacts/$', 'contact.views.my_contact', name='wtfcontacts'),
    url(r'^received/$', 'contact.views.received', name='received'), 
)