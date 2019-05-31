from django.urls import path, include

from .views import *

urlpatterns = [
    path('', archive, name="archive"),
]