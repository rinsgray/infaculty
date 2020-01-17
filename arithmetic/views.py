from django.shortcuts import render, get_object_or_404
from random import randint, choice
from django.http import HttpResponse
from .models import Rule, Student, QuestionWithSelection
# Create your views here.

def index(request):
    return render(request, 'arithmetic/index.html',{})

def equations(request):
    try:
        QWS = QuestionWithSelection.objects.order_by('?').first()
    except Exception:
        QWS = None
    QWStext = QWS.QWS_text
    QWSans  = QWS.selection_set.all().order_by('?')
    return render(request, 'arithmetic/equations.html',{'QWStext':QWStext,'QWSans':QWSans})

def arithmetic(request):
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
    return render(request, 'arithmetic/arithmetic.html',{'left':left,'right':right,'answer':answer,'sign':sign})

def exercise(request):
    return render(request, 'arithmetic/exercise.html',{})

def rule_detail(request, pk):
    rule = get_object_or_404(Rule, pk=pk)
    return render(request, 'arithmetic/rule_detail.html',{'rule':rule})

def rules(request,pk=None):
    rules = Rule.objects.all()
    if pk:
        rules = Rule.objects.filter(tags__name__in=[str(pk)])
    alltags=[]
    for rule in rules:
        for tag in rule.tags.all():
            if tag not in alltags:
                alltags.append(tag)
    return render(request, 'arithmetic/rules.html',{'rules':rules,'alltags':alltags})
'''
def rules_filtered(request,t):
    rules = Rule.objects.filter(tags__name__in=[str(t)])
    alltags=[]
    for rule in rules:
        for tag in rule.tags.all():
            if tag not in alltags:
                alltags.append(tag)
    return render(request, 'arithmetic/rules.html',{'rules':rules,'alltags':alltags})
'''

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'arithmetic/student_detail.html',{'student':student})

def students(request):
    students = Student.objects.all()
    return render(request, 'arithmetic/students.html',{'students':students})
