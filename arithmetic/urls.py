from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('exercise/', views.exercise, name='exercise'),
    path('rule<int:pk>/', views.rule_detail, name='rule_detail'),
    path('rules/', views.rules, name='rules'),
    path('student<int:pk>/', views.student_detail, name='student_detail'),
    path('students/', views.students, name='students')
]
