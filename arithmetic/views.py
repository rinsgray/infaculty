from django.shortcuts import render, get_object_or_404
from random import randint, choice
from django.http import HttpResponse
from .models import Rule, Student
# Create your views here.

def index(request):
    return render(request, 'arithmetic/index.html',{})

def exercise(request):
    left=randint(10,40)
    right=randint(2,10)
    sign=choice(['+','*','-','/'])
    if sign=='*':
        answer=left*right
    elif sign=='+':
        answer=left+right
    elif sign=='-':
        answer=left-right
    elif sign=='/':
        while left%right!=0:
            left=randint(10,40)
            right=randint(2,10)
        answer=left//right

    #return HttpResponse(str(left)+'*'+str(right))
    return render(request, 'arithmetic/exercise.html',{'left':left,'right':right,'answer':answer,'sign':sign})

def rule_detail(request, pk):
    rule = get_object_or_404(Rule, pk=pk)
    return render(request, 'arithmetic/rule_detail.html',{'rule':rule})

def rules(request):
    rules = Rule.objects.all()
    return render(request, 'arithmetic/rules.html',{'rules':rules})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'arithmetic/student_detail.html',{'student':student})

def students(request):
    students = Student.objects.all()
    return render(request, 'arithmetic/students.html',{'students':students})
