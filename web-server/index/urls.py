from django import urls
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_r, name='index'),
]