from django.shortcuts import render, get_object_or_404

from models import Post


def list(request):
    data = {'posts': Post.objects.filter(published=True)}

    return render(request, 'posts_list.html', data)

def detail(request, pk):
    data = {'post': get_object_or_404(Post, pk=pk)}

    return render(request, 'posts_detail.html', data)
