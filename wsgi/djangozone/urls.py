from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'posts.views.list', name='posts_list'),
    url(r'^posts/', include('posts.urls')),
    url(r'^about/$', 'common.views.about', name='about'),

    url(r'^admin/', include(admin.site.urls)),
)
