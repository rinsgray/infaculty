from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('exercise/', views.exercise, name='exercise'),
    path('rule<int:pk>/', views.rule_detail, name='rule_detail'),
    path('rules/', views.rules, name='rules'),
    path('student<int:pk>/', views.student_detail, name='student_detail'),
    path('students/', views.students, name='students'),
    path('arithmetic/', views.arithmetic, name='arithmetic'),
    path('formulas/<int:pk>', views.formulas, name='formulas'),
    path('test/',views.formulas_forms,name='formulas_forms')
#    path('filtered/', views.rules_filtered, name='rules_filtered'),
]
