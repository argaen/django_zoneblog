from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

import views

urlpatterns = patterns(
    '',
    url(r'^$', views.PostListView.as_view(), name='post-list'),
    url(r'^(?P<slug>[\w-]+)/$', views.PostDetailView.as_view(), name='post-detail'),

    url(r'^about/$', 'about', name='about'),
)

urlpatterns = urlpatterns + patterns('django.views.generic.simple',
    # (r'^projects/catalonia-9n-results/$', TemplateView.as_view(template_name='projects/9n/9n.html')),
    (r'^projects/9n/stats.html$', TemplateView.as_view(template_name='projects/9n/stats.html')),
)
