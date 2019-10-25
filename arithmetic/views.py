from django.shortcuts import render
from random import randint, choice
from django.http import HttpResponse
from .models import Rule
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
