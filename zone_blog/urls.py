from django.conf.urls import patterns, url

import views
import feeds

urlpatterns = patterns(
    '',
    url(r'^posts$', views.PostListView.as_view(), name='post-list'),
    url(r'^posts/rss/(?P<tag>[\ \w-]+)/$', feeds.Category()),
    url(r'^posts/rss/', feeds.LatestPosts()),
    url(r'^posts/tag/(?P<tag>[\ \w-]+)/$', views.PostListView.as_view(), name='post-list-tag'),
    url(r'^posts/archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.PostListView.as_view(), name='post-list-archive'),
    url(r'^posts/(?P<slug>[\w-]+)/$', views.PostDetailView.as_view(), name='post-detail'),

    url(r'^projects$', views.ProjectListView.as_view(), name='project-list'),
    url(r'^projects/tag/(?P<tag>[\ \w-]+)/$', views.ProjectListView.as_view(), name='project-list-tag'),
    url(r'^projects/archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.ProjectListView.as_view(), name='project-list-archive'),
    url(r'^projects/(?P<slug>[\w-]+)/$', views.ProjectDetailView.as_view(), name='project-detail'),


    # url(r'^about/$', 'views.about', name='about'),
)
