from django.shortcuts import render
from django.template import RequestContext

from models import Post

def list(request):
    data = {'posts': Post.objects.filter(published=True)}

    return render(request, 'home.html', data)
