from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'posts.views',
    url(r'^$', 'list', name='posts_list'),
    url(r'^(?P<slug>[\w-]+)$', 'detail', name='posts_detail'),

    url(r'^tag/(?P<tag>\w+)$', 'tags', name='posts_tags'),
)
