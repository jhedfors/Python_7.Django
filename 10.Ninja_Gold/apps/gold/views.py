from django.shortcuts import render, redirect
import random
import datetime

def index(request):
    if 'score' not in request.session:
        request.session['score'] = 0
    if 'actions' not in request.session:
        request.session['actions'] = ['']
    context = {'score': request.session['score'], 'actions': request.session['actions']}
    return render(request, 'index.html', context)
def process_money(request):
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %I:%M %p")
    print current_time
    print datetime.datetime.now()
    if request.POST['building'] == 'farm':
        randNum = random.randrange(10,21)
        request.session['score'] += randNum
        request.session['actions'].insert(0,"Earned " + str(randNum)+ " golds from the farm! ("+current_time+")")
    if request.POST['building'] == 'cave':
        randNum = random.randrange(5,11)
        request.session['score'] += randNum
        request.session['actions'].insert(0,"Earned " + str(randNum)+ " golds from the cave! ("+current_time+")")
    if request.POST['building'] == 'house':
        randNum = random.randrange(2,6)
        request.session['score'] += randNum
        request.session['actions'].insert(0,"Earned " + str(randNum)+ " golds from the house! ("+current_time+")")
    if request.POST['building'] == 'casino':
        if random.randrange(0,2) == 1:
            randNum = random.randrange(0,51)
            request.session['score'] += randNum
            request.session['actions'].insert(0,"Earned " + str(randNum)+ " golds from the casino! ("+current_time+")")
        else:
            randNum = random.randrange(0,51)
            request.session['score'] -= randNum
            request.session['actions'].insert(0,"Lost " + str(randNum)+ " golds from the casino! ("+current_time+")")
    return redirect('/')
def reset(request):
    del request.session['actions']
    del request.session['score']
    return redirect('/')
