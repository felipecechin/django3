from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('tag/<tag>', index, name='index_tagged'),
    path('<slug:slug>', thread, name='thread'),
]
