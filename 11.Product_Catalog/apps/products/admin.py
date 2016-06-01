from django.contrib import admin
from .models import Product, Manufacturer
from . import models

admin.site.register(Product)
admin.site.register(Manufacturer)
