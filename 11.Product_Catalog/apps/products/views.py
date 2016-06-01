from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from django.views.generic import View
class index(View):
    errors = {}
    def get(self,request):
        self.errors = {}
        manufacturers = models.Manufacturer().index()
        products = models.Product().index()
        error_messages = messages.get_messages(request)
        for message in error_messages:
            self.errors[message.extra_tags] = str(message)
        context = {'manufacturers': manufacturers, 'products':products, 'errors':self.errors}
        return render(request, 'products/index.html', context)
    def post(self,request):
        errors = models.Product().create(request.POST)
        if errors:
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
