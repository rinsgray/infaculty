from django.shortcuts import render
from random import randint
from django.http import HttpResponse
# Create your views here.

def exercise(request):
    left=randint(10,50)
    right=randint(10,50)
    answer=left*right
    #return HttpResponse(str(left)+'*'+str(right))
    return render(request, 'arithmetic/exercise.html',{'left':left,'right':right,'answer':answer})

def checkanswer(request):
