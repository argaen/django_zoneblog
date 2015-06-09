from django.views.generic import DetailView
from django.views.generic.dates import ArchiveIndexView

from taggit.models import Tag

from models import Post, Project
from mixins import TaggedObjectMixinView, DateObjectMixinView, DraftObjectMixinView


class PostListView(TaggedObjectMixinView, DateObjectMixinView, DraftObjectMixinView, ArchiveIndexView):
    context_object_name = 'objects'
    template_name = 'post_list.html'
    queryset = Post.objects.all()
    paginate_by = 4
    date_field = 'published_on'


class PostDetailView(TaggedObjectMixinView, DateObjectMixinView, DraftObjectMixinView, DetailView):

    context_object_name = 'o'
    slug_field = 'slug'
    template_name = 'post_detail.html'
    queryset = Post.objects.all()


class ProjectListView(TaggedObjectMixinView, DateObjectMixinView, DraftObjectMixinView, ArchiveIndexView):
    context_object_name = 'objects'
    template_name = 'project_list.html'
    queryset = Project.objects.all()
    date_field = 'published_on'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['categories'] = Tag.objects.filter(project__is_published=True)
        return context


class ProjectDetailView(TaggedObjectMixinView, DateObjectMixinView, DraftObjectMixinView, DetailView):

    context_object_name = 'o'
    slug_field = 'slug'
    template_name = 'project_detail.html'
    queryset = Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['objects'] = Project.objects.filter(is_published=True).exclude(pk=self.get_object().pk)
        return context
