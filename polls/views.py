from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world,at polls index")

def detail(request,question_id):
    return HttpResponse("you're looking at question %s. "%question_id)

def results(request,question_id):
    reponse="you're loking at the result of question %s."
    return HttpResponse(reponse % question_id)
def vote(request,quetion_id):
    return HttpResponse("you're voting on question %s." % quetion_id)