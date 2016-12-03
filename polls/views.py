from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Question, Choice
# Create your views here.


def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'lastest_question_list': lastest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        seleted_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select choice.",
        })
    else:
        seleted_choice.votes += 1
        seleted_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))

