# there will be a bunch of comments here that explain adding new routes to the urls
#just make sure you find the code below and add the line
from django.conf.urls import include, url
from . import views
app_name= 'users'
urlpatterns = [
  url(r'^login/$', views.login, name='login'),
]
