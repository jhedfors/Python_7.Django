from django.shortcuts import render, redirect
import random
from django.utils.crypto import get_random_string
import string
def index(request):
    info ={}
    return render(request,'index.html', info)
def random(request):
    randStr = get_random_string(length = 14).upper()
    context = {'randStr': randStr}
    print 'context:', context['randStr']
    print request.session['counter']
    if 'counter' not in request.session:
    	request.session['counter'] = 1
    else :
    	request.session['counter'] += 1
    return render(request,'index.html', context)
def reset(request):
    request.session['counter'] = 0
    return redirect('/random')
