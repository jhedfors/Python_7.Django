from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

def index(request):
    error_messages = messages.get_messages(request)
    errors = {}
    for message in error_messages:
        errors[message.extra_tags] = str(message)
    manufacturers = models.Manufacturer().index()
    products = models.Product().index()
    context = {'manufacturers': manufacturers, 'products':products, 'errors':errors}
    return render(request, 'products/index.html', context)
def create(request):
    errors = models.Product().create(request.POST)
    for error in errors:
        messages.error(request, errors[error], extra_tags=error)
    return redirect('/products')
def edit_view(request,id):
    manufacturers = models.Manufacturer().index()
    product = models.Product().show(id)
    context = {'product': product, 'manufacturers' : manufacturers}
    return render(request, 'products/edit.html', context)
def edit(request):
    models.Product().update(request.POST)
    return redirect('/products')
def delete(request,id):
    models.delete(id)
    return redirect('/products')