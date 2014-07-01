from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'posts.views',
    url(r'^$', 'list', name='posts_list'),
    url(r'^(?P<pk>[\w-]+)$', 'detail', name='posts_detail'),
)
