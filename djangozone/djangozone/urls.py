from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'zone_blog.views.contents_list', name='contents_list'),
    url(r'^zone_blog/', include('zone_blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('zone_blog.urls')),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        )
