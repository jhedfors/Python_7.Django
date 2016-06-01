from django.contrib import admin # import the admin module
from .models import User, Interest # import the models from the models.py file
# then we will will register the models to our Admin Site
admin.site.register(User)
admin.site.register(Interest)
