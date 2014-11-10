from django.conf.urls import patterns
from django.views.generic import TemplateView

urlpatterns = patterns('django.views.generic.simple',
    (r'^$', TemplateView.as_view(template_name='9n/9n.html')),
    (r'^9n/$', TemplateView.as_view(template_name='9n/9n.html')),
    (r'^9n/stats.html$', TemplateView.as_view(template_name='9n/stats.html')),
)
