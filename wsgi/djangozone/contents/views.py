from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Post, NewsItem


def posts_list(request):
    posts = Post.objects.filter(published=True)
    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    data = {'objects': posts}

    return render(request, 'contents_list.html', data)


def posts_detail(request, slug):
    data = {'object': get_object_or_404(Post, slug=slug)}

    return render(request, 'contents_detail.html', data)


def posts_tags(request, tag):
    data = {'objects': Post.objects.filter(tags__name__in=[tag])}

    return render(request, 'contents_list.html', data)


def news_list(request):
    news = NewsItem.objects.filter(published=True)
    paginator = Paginator(news, 5)

    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    data = {'objects': news}

    return render(request, 'contents_list.html', data)


def news_detail(request, slug):
    data = {'object': get_object_or_404(NewsItem, slug=slug)}

    return render(request, 'contents_detail.html', data)


def news_tags(request, tag):
    data = {'objects': NewsItem.objects.filter(tags__name__in=[tag])}

    return render(request, 'contents_list.html', data)