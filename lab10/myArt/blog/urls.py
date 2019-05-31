from django.urls import path, include

from .views import *

urlpatterns = [
    path('', archive, name="archive"),
    path('<int:article_id>', get_article, name="get-article"),
    path('new/', create_post, name="create_post"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),
]