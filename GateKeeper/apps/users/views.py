from django.http import HttpResponse, Http404
from django.shortcuts import render

def login(request):
    print request.POST
    info = {}
    return render(request,'users/login.html', info)
