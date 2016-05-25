from django.shortcuts import render

def index(request):
    content = {}
    return render(request, 'ninjas/index.html', content)
def ninjas(request, ninja_name):
    name = ninja_name
    if name == 'all':
        ninja = 'all'
    elif name == 'blue':
        ninja = 'blue'
    elif name == 'orange':
        ninja = 'orange'
    elif name == 'red':
        ninja = 'red'
    elif name == 'purple':
        ninja = 'purple'
    else:
        ninja = 'none'
    content = {'ninja':ninja}
    print content
    return render(request,"ninjas/ninjas.html",content)
