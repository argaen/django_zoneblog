from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

from zone_blog import views as blog_views

urlpatterns = patterns(
    '',
    url(r'^$', blog_views.PostListView.as_view(), name='home'),
    url(r'^blog/', include('zone_blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        )
