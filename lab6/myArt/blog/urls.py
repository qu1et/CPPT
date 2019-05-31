from django.urls import path, include

from .views import *

urlpatterns = [
    path('', archive, name="archive"),
    path('<int:article_id>', get_article, name="get-article"),
]