from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from .models import Articles

# Create your views here.

def archive(request):
    posts = Articles.objects.all()
    return render(request, 'blog/archive.html', {"posts": posts})

def get_article(request, article_id):    
    try:        
        post = Articles.objects.get(id=article_id)        
        return render(request, 'blog/article.html', {"post": post})    
    except Articles.DoesNotExist:        
        raise Http404
