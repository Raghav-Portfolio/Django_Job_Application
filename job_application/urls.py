from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')  # connect the home page to views.index function
]
