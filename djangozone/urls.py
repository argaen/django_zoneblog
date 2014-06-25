from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^posts$', 'posts.views.list', name='posts_list'),
    url(r'^posts/(?P<pk>[\w-]+)$', 'posts.views.detail', name='posts_detail'),

    url(r'^admin/', include(admin.site.urls)),
)
