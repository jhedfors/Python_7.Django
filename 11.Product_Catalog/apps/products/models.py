from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=25)
    created_at = models.DateField()
    updated_at = models.DateField()
    def index(self):
        manufacturers = Manufacturer.objects.all()
        return manufacturers
class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    def index(self):
        products = Product.objects.all()
        return products
    def show(self,id):
        product = Product.objects.get(id=id)
        return product
    def create(self,post):
        errors = {}
        if len(post['name'])<8:
            errors['name'] = u'Product Name cannot be empty'
        if len(post['description'])<1:
            errors['description'] = u'Description cannot be empty'
        if len(errors) > 0:
            return errors
        manufacturer = Manufacturer.objects.get(id=post['manufacturer'])
        new = Product(manufacturer = manufacturer, name = post['name'], price = post['price'], description = post['description'],updated_at = timezone.now() , created_at = timezone.now())
        new.save()
        return
    def update(self,post):
        manufacturer = Manufacturer.objects.get(id=post['manufacturer'])
        item = Product.objects.get(id=post['id'])
        item.manufacturer = manufacturer
        item.name = post['name']
        item.price = post['price']
        item.description = post['description']
        item.updated_at = timezone.now()
        item.save()
        return
def delete(id):
    return Product.objects.get(id=id).delete()
