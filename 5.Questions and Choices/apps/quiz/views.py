from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect # inserted this line
from . models import Question, Choice
from django.utils import timezone
def index(request):
  questions = Question.objects.all()
  context = {'questions': questions}
  return render(request, 'quiz/index.html', context)
def show(request, question_id):
  question = Question.objects.get(id = question_id)
  print question.id
  context = {
    'id': question.id,
    'question': question.question_text,
  }
  return render(request, 'quiz/show.html', context)

def add_question(request):
    info = 'With Choices?'
    question = Question(question_text=info, pub_date = timezone.now())
    question.save()
    choice = Choice(choice_text = 'This is a choice', question = question)
    choice.save()
    return redirect('.')
