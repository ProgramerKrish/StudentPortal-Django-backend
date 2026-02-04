from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions
from django.template import loader

def index(request):
    latest_question_list=Questions.objects.order_by("-pub_date")[:5]
    """ output=", ".join([q.question_text for q in latest_question_list]) """
    template=loader.get_template("polls/index.html")
    context={"latest_question_list":latest_question_list}
    """ return HttpResponse(template.render(context,request)) """
    return render(request,"polls/index.html",context)
def detail(request,question_id):
    return HttpResponse("you're looking at question %s. "%question_id)

def results(request,question_id):
    reponse="you're loking at the result of question %s."
    return HttpResponse(reponse % question_id)
def vote(request,quetion_id):
    return HttpResponse("you're voting on question %s." % quetion_id)

