from django.shortcuts import render, redirect

def index(request):
    return render(request,'surveys/index.html')
def process_form(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] +=1
    info = {'name' : request.POST['name'],
    'location' : request.POST['location'],
    'language' : request.POST['language'],
    'comment' : request.POST['comment'],
    'count' : request.session['count']}
    request.session['info'] = info
    return redirect('/result')
def result(request):
    info = request.session['info']
    return render(request,'surveys/result.html',info)
def reset_count(request):
    request.session['count'] = 0
    return redirect('/')
