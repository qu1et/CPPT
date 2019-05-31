from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from .models import Articles

# Create your views here.

def archive(request):
    posts = Articles.objects.all()
    return render(request, 'blog/archive.html', {"posts": posts})
    