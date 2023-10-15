from unicodedata import name
from django.urls import path, include

from . import views

urlpatterns = [
    #index page
    path('', views.index, name='index'),
]