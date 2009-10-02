from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$', 'bicalca.monitor.views.show'),
    (r'^monitor/add', 'bicalca.monitor.views.add'),
    (r'^monitor/save', 'bicalca.monitor.views.save'),
    (r'^hasser/$', 'bicalca.needs.views.show'),
    (r'^hasser/add', 'bicalca.needs.views.add'),
    (r'^hasser/save', 'bicalca.needs.views.save'),
    (r'^hasser/bought', 'bicalca.needs.views.bought'),
    (r'^login/$', 'bicalca.monitor.views.login_first'),
    (r'^log/$', 'bicalca.monitor.views.log'),
    (r'^out/$', 'bicalca.monitor.views.out'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
