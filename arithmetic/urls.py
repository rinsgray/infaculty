from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('exercise/', views.exercise, name='exercise'),
    path('rules/', views.rules, name='rules')
]
