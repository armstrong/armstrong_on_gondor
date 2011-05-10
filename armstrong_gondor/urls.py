from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from armstrong.core.arm_wells.views import SimpleWellView

import armstrong.apps.arm_events.urls as event_urls

urlpatterns = patterns('',
    url(r'^contact/', include('contact_form.urls')),
    url(r'^$','django.views.generic.simple.direct_to_template',{'template':'index.html'}),
    url(r'^well/$', SimpleWellView.as_view(template_name='home/index.html',
                                      well_title='Generic'), name='welltest'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', include(event_urls)),
)
