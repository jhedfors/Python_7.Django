from django.shortcuts import render
# from datetime import datetime, time
from django.utils import timezone
from models import Interest, User
def index(request):
    # 1 show all interests
    interests = Interest.objects.all()
    # 2 show all users
    users = User.objects.all()
    # 3 insert a new interest
    # interest1 = Interest(name='Skiing', created_at = timezone.now())
    # interest1.save()
    # interest2 = Interest(name='Legos', created_at = timezone.now())
    # interest2.save()
    # 4 insert a new user
    # User1 = User(first_name='Jeff', last_name='Hedfors', age=48, occupation ="Full Stack Web Developer", interest = Interest.objects.get(id=1), created_at = timezone.now())
    # User1.save()
    # User2 = User(first_name='Billy', last_name='Jones', age=5, occupation ="n/a", interest = Interest.objects.get(id=2), created_at = timezone.now())
    # User2.save()
    # 5 Select one interest that has id = 1
    print 'GET:', User.objects.get(id=1)
    # users = User.objects.filter(id=1)
    # 6 Select all the users whose first name starts with a "J"
    # users = User.objects.filter(first_name__startswith="B")
    # 7 Select all the users with age > 25
    # users = User.objects.filter(age__gt=25)
    # 8 Select all the users created in the year 2016
    # users = User.objects.filter(created_at__year=2016)
    # 9 Update user with id = 2, and set age to 26
    # user2 = User.objects.get(id=2)
    # user2.age = 26
    # user2.first_name = 'William'
    # user2.interest = Interest.objects.get(id=1)
    # user2.save()
    # users = User.objects.all()
    context = {'users': users, 'interests': interests}
    return render(request,'interests/index.html',context)
