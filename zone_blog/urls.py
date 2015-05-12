from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

import views

urlpatterns = patterns(
    '',
    url(r'^posts$', views.PostListView.as_view(), name='post-list'),
    url(r'^posts/tag/(?P<tag>[\ \w-]+)/$', views.PostListView.as_view(), name='post-list-tag'),
    url(r'^posts/(?P<slug>[\w-]+)/$', views.PostDetailView.as_view(), name='post-detail'),

    # url(r'^projects$', views.ProjectListView.as_view(), name='project-list'),
    # url(r'^projects/(?P<slug>[\w-]+)/$', views.ProjectDetailView.as_view(), name='project-detail'),

    # url(r'^about/$', 'views.about', name='about'),
)

urlpatterns = urlpatterns + patterns('django.views.generic.simple',
    # (r'^projects/catalonia-9n-results/$', TemplateView.as_view(template_name='projects/9n/9n.html')),
    (r'^projects/9n/stats.html$', TemplateView.as_view(template_name='projects/9n/stats.html')),
)
