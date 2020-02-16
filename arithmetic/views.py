from django.shortcuts import render, get_object_or_404
from random import randint, choice
from django.http import HttpResponse
from .models import Rule, Student, QuestionWithSelection, Subject
# Create your views here.

def index(request):
    subjects = Subject.objects.all()
    return render(request, 'arithmetic/index.html',{'subjects':subjects})

def formulas(request, pk, pre_right = 0, pre_total = 0):
    QWS = QuestionWithSelection.objects.filter(QWS_subject=pk).order_by('?').first()
    QWStext = QWS.QWS_text
    QWSans  = QWS.selection_set.all().order_by('?')
    subjects = Subject.objects.all()
    return render(request, 'arithmetic/equations.html',{'QWStext':QWStext,'QWSans':QWSans, 'subjects':subjects,'pre_right':pre_right,'pre_total':pre_total,'subject':pk})


def formulas_forms(request):
    try:
        QWS = QuestionWithSelection.objects.order_by('?').first()
    except Exception:
        QWS = None
    QWStext = QWS.QWS_text
    QWSans  = QWS.selection_set.all().order_by('?')
    subjects = Subject.objects.all()
    return render(request, 'arithmetic/formulas.html',{'QWStext':QWStext,'QWSans':QWSans, 'subjects':subjects})


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
    subjects = Subject.objects.all()
    return render(request, 'arithmetic/arithmetic.html',{'left':left,'right':right,'answer':answer,'sign':sign, 'subjects':subjects})

def exercise(request):
    subjects = Subject.objects.all()
    return render(request, 'arithmetic/exercise.html',{'subjects':subjects})

def rule_detail(request, pk):
    rule = get_object_or_404(Rule, pk=pk)
    subjects = Subject.objects.all()
    return render(request, 'arithmetic/rule_detail.html',{'rule':rule, 'subjects':subjects})

def rules(request,pk=None):
    rules = Rule.objects.all()
    if pk:
        rules = Rule.objects.filter(tags__name__in=[str(pk)])
    alltags=[]
    for rule in rules:
        for tag in rule.tags.all():
            if tag not in alltags:
                alltags.append(tag)
    subjects = Subject.objects.all()
    return render(request, 'arithmetic/rules.html',{'rules':rules,'alltags':alltags, 'subjects':subjects})
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
    subjects = Subject.objects.all()
    return render(request, 'arithmetic/student_detail.html',{'student':student, 'subjects':subjects})

def students(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'arithmetic/students.html',{'students':students, 'subjects':subjects})
