from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ex1/<str:son>', views.ex1, name='home'),
    path('ex2/<str:son>', views.ex2, name='index'),
]
