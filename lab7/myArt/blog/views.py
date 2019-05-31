from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

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

def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST': #меняете на гет в вашем случае
        # обработать данные если метод POST
            form = {
                'text' : request.POST['text'], #так же только request.GET т.к. <input type="text" name="text"> имя поля text и в request.GET оно лежит
                'title' : request.POST['title'] # тут вместо title из GET берите name="priority" 'priority' : request.POST['priority']
            }

            if (check(form['title']) == True):
                form['errors'] = u'Статья с таким названием уже есть!'
                return render(request, 'blog/create_post.html', {'form':form})
            else:
        # в словаре form будет храниться введенная информация
                if form['text'] and form['title']:
        # если поля заполнены без ошибок
                    Articles.objects.create( # создаете запись в бд 
                        text=form['text'],
                        title=form['title'],
                        author=request.user)
            #достаю только что созданную статью с целью получения ее id и редиректа на страницу с ней
                    article = Articles.objects.get(title=form['title'])
                    return redirect('get-article', article_id = article.id)
                else:
            # Если данные не корректны
                    form['errors'] = u'Не все поля заполнены'
                    return render(request, 'blog/create_post.html', {'form': form})
        else:
            return render(request, 'blog/create_post.html', {})
    else:
        raise Http404

def check(nem):
    try:
        article = Articles.objects.get(title = nem)
        if(nem == article.title):
            return True
        else:
            return False

    except Articles.DoesNotExist:
        return False