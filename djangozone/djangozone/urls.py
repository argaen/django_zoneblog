from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'djzone_blog.views.contents_list', name='contents_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^djzone_blog/', include('djzone_blog.urls')),

    url(r'', include('djzone_blog.urls')),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        )
