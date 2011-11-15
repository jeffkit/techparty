from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'site_media/(?P<path>.*)','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    (r'^$', 'core.views.index'),
    (r'^admin/', include(admin.site.urls)),                       
    (r'^events/','core.views.events'),
    (r'^event/(?P<id>\d+)/$','core.views.event'),
    (r'^enroll/(?P<eid>\d+)/$','core.views.enroll'),
)
