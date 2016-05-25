from django.shortcuts import render

def index(request):
    content = {}
    return render(request, 'ninjas/index.html', content)
def ninjas(request, ninja_color = ''):
    if ninja_color == '':
        ninja = 'all'
    elif ninja_color == 'blue':
        ninja = 'blue'
    elif ninja_color == 'orange':
        ninja = 'orange'
    elif ninja_color == 'red':
        ninja = 'red'
    elif ninja_color == 'purple':
        ninja = 'purple'
    else:
        ninja = 'none'
    content = {'ninja':ninja}
    return render(request,"ninjas/ninjas.html",content)
