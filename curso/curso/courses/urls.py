from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', details, name='details'),
    path('<slug:slug>/inscricao', enrollment, name='enrollment'),
    path('<slug:slug>/anuncios', announcements, name='announcements'),
    path('<slug:slug>/anuncios/<int:pk>/', show_announcement, name='show_announcement'),
    path('<slug:slug>/cancelar-inscricao', undo_enrollment, name='undo_enrollment'),
]

