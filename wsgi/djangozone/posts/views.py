from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Post


def list(request):
    posts = Post.objects.filter(published=True)
    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    data = {'posts': posts}

    return render(request, 'posts_list.html', data)


def detail(request, slug):
    data = {'post': get_object_or_404(Post, slug=slug)}

    return render(request, 'posts_detail.html', data)


def tags(request, tag):
    data = {'posts': Post.objects.filter(tags__name__in=[tag])}

    return render(request, 'posts_list.html', data)
