# there will be a bunch of comments here that explain adding new routes to the urls
#just make sure you find the code below and add the line
from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
  url(r'^quiz/', include('apps.quiz.urls')), # we inserted this line!!!
  url(r'admin/', include(admin.site.urls)),
]
