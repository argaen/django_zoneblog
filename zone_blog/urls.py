from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    'zone_blog.views',
    url(r'^posts/$', 'posts_list', name='posts_list'),
    url(r'^posts/tag/(?P<tag>\w+)$', 'posts_list', name='posts_tags'),
    url(r'^posts/(?P<slug>[\w-]+)$', 'posts_detail', name='posts_detail'),

    url(r'^news/$', 'news_list', name='newsitems_list'),
    url(r'^news/tag/(?P<tag>\w+)$', 'news_list', name='newsitems_tags'),
    url(r'^news/(?P<slug>[\w-]+)$', 'news_detail', name='newsitems_detail'),

    url(r'^projects/$', 'projects_list', name='projects_list'),
    url(r'^projects/tag/(?P<tag>\w+)$', 'projects_list', name='projects_list'),
    url(r'^projects/(?P<slug>[\w-]+)$', 'projects_detail', name='projects_detail'),

    url(r'^about/$', 'about', name='about'),
)

urlpatterns = urlpatterns + patterns('django.views.generic.simple',
    # (r'^projects/catalonia-9n-results/$', TemplateView.as_view(template_name='projects/9n/9n.html')),
    (r'^projects/9n/stats.html$', TemplateView.as_view(template_name='projects/9n/stats.html')),
)
