from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'contact.views.home', name='home'),
    url(r'^census/', include('census.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

