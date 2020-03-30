from django.urls import path

from .views import home, contato

urlpatterns = [
    path('news/', home, name='home'),
    path('contato/', contato, name='contato'),
]
