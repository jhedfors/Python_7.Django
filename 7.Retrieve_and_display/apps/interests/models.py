from __future__ import unicode_literals
from datetime import datetime, time
from django.db import models

class Interest(models.Model):
    # id, name, created_at
    # select all, Insert
    # Select one interest that has id=1 (Hint: use the get() function)
    name = models.TextField(max_length=100)
    created_at = models.DateTimeField(datetime.now())

class User(models.Model):
    # id, first_name, last_name, age, created_at, occupation, interest (key = id)
    # select all,Insert
    # Select all the users whose first name starts with a "J"
    # Select all the users with age > 25
    # Select all the users created in the year 2015
    # Update user with id = 5, and set age to 26
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    age = models.IntegerField()
    occupation = models.TextField(max_length=20)
    interest = models.ForeignKey(Interest)
    created_at =models.DateTimeField()
    # def __str__(self):
    #     return 'name: %s %s' % (self.first_name, self.last_name)
