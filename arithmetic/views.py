from django.shortcuts import render
from random import randint, choice
from django.http import HttpResponse
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

def rules(request):
    return render(request, 'arithmetic/rules.html',{})
