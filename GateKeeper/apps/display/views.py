from django.shortcuts import render

def index(request):
    info = {}
    return render(request,'display/index.html', info)
