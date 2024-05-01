from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context) #render does not require loader or template var

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("question does not exist")
    return render(request, "polls/detail.html",
    {"question": question}) # render(request, template directory, context)


def results(request, question_id):
    results = get_object_or404(Choice.objects.all()) # get_object_or_404 shortcut for try except method, get_list_or_404 does the same except using .filter instead of .get 
    return render(request, "polls/results.html"), {"results":results}


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
