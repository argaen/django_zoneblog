from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'contents.views.contents_list', name='contents_list'),
    url(r'^contents/', include('contents.urls')),
    url(r'^about/$', 'common.views.about', name='about'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdownx/', include('markdownx.urls')),

    url(r'', include('contents.urls')),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        )
