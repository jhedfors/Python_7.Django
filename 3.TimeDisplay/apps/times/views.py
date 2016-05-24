from django.shortcuts import render
import datetime

def index(request):
    current_time = datetime.datetime.now()
    content = {'current_time': current_time}
    return render(request, 'times/index.html',content)
