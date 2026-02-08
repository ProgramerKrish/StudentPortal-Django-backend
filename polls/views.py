from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Questions
from django.http import Http404
from django.template import loader

def index(request):
    latest_question_list=Questions.objects.order_by("-pub_date")[:5]
    
    template=loader.get_template("polls/index.html")
    context={"latest_question_list":latest_question_list}
    """ return HttpResponse(template.render(context,request)) """
    return render(request,"polls/index.html",context)


def detail(request,question_id):
    """ try:
       question=Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
       raise Http404("question does not exist") """
    question=get_object_or_404(Questions, pk=question_id)
    
    return render(request,"polls/details.html",{"question":question})


def results(request,question_id):
    reponse="you're loking at the result of question %s."
    return HttpResponse(reponse % question_id)


def vote(request,quetion_id):
    return HttpResponse("you're voting on question %s." % quetion_id)

