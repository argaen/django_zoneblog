from operator import attrgetter
from itertools import chain

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Post, NewsItem, Content, Project

def contents_list(request, tag=None):
    if tag:
        contents = sorted(
                    chain(Post.objects.filter(published=True, tags__name__in=[tag]),
                        NewsItem.objects.filter(published=True, tags__name__in=[tag]),
                        Project.objects.filter(published=True, tags_name__in=[tag])),
                    key=attrgetter('published_on'), reverse=True)
    else:
        contents = sorted(
            chain(Post.objects.filter(published=True), NewsItem.objects.filter(published=True), Project.objects.filter(published=True)),
            key=attrgetter('published_on'), reverse=True)
    paginator = Paginator(contents, 5)

    page = request.GET.get('page')
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        contents = paginator.page(1)
    except EmptyPage:
        contents = paginator.page(paginator.num_pages)

    data = {'objects': contents}

    return render(request, 'contents_list.html', data)

def posts_list(request, tag=None):
    if tag:
        posts = Post.objects.filter(published=True, tags__name__in=[tag])
    else:
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
    data = {'objects': get_object_or_404(Post, slug=slug)}

    return render(request, 'contents_list.html', data)


def news_list(request, tag=None):
    if tag:
        news = NewsItem.objects.filter(published=True, tags__name_in=[tag])
    else:
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
    data = {'objects': get_object_or_404(NewsItem, slug=slug)}

    return render(request, 'contents_list.html', data)


def projects_list(request, tag=None):

    if tag:
        projects = Project.objects.filter(published=True, tags__name__in=[tag])
    else:
        projects = Project.objects.filter(published=True)
    paginator = Paginator(projects, 5)

    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    data = {'objects': projects}

    return render(request, 'contents_list.html', data)


def projects_detail(request, slug):
    data = {'objects': get_object_or_404(Project, slug=slug)}

    return render(request, 'contents_list.html', data)
