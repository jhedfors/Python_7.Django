from django.shortcuts import render

def index(request):
    context = {}
    return render(request,'interests/index.html',context)
