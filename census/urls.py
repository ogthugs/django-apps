from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^wtfcensus/$', 'census.views.my_census', name='wtfcensus'),
    url(r'^received/$', 'census.views.received', name='received'), 
)