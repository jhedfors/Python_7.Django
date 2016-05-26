from django.shortcuts import render
from django.utils import timezone
from models import Interest, User
def index(request):
    return render(request,'interests/index.html')
def user(request,user_id):
    user = User.objects.get(id=user_id)
    context = {'user': user}
    return render(request,'interests/user.html',context)
def interests(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request,'interests/interests.html',context)
