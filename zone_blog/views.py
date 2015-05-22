from django.views.generic import DetailView
from django.views.generic.dates import ArchiveIndexView


from models import Post, Project


class PostListView(ArchiveIndexView):
    context_object_name = 'objects'
    template_name = 'content_list.html'
    queryset = Post.objects.filter(is_published=True)
    paginate_by = 4
    date_field = 'published_on'

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        if "tag" in self.kwargs:
            queryset = queryset.filter(tags__name__in=[self.kwargs["tag"]])

        if "year" in self.kwargs and "month" in self.kwargs:
            queryset = queryset.filter(published_on__year=self.kwargs["year"], published_on__month=self.kwargs["month"])

        return queryset


class PostDetailView(DetailView):

    context_object_name = 'o'
    slug_field = 'slug'
    template_name = 'content_detail.html'
    queryset = Post.objects.filter(is_published=True)


# class ProjectListView(ArchiveIndexView):
#     context_object_name = 'objects'
#     template_name = 'content_list.html'
#     queryset = Project.objects.filter(is_published=True)
#     paginate_by = 4
#     date_field = 'published_on'


# class ProjectDetailView(DetailView):

#     context_object_name = 'o'
#     slug_field = 'slug'
#     template_name = 'content_detail.html'
#     queryset = Project.objects.filter(is_published=True)
