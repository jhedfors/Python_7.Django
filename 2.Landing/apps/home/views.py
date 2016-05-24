from django.shortcuts import render

def index(request):
    content = {'name':'Michael Choi', 'hobby': 'Play Basketball', 'language':'Python'}
    return render(request, "quiz/index.html",content)
