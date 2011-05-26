from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from armstrong.core.arm_wells.views import SimpleWellView

#from armstrong.apps import events

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^events/', include(events.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^$', SimpleWellView.as_view(template_name='home/index.html',
                                      well_title='Generic'), name='home'),
   
)