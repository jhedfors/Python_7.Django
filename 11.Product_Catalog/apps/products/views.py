from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from django.views.generic import View
class Index(View):
    def get(self,request):
        if request.session.get('errors'): #If session errors exist...
            errors = dict(request.session.get('errors')) #copying dict to 'error' so I can delete session error
            del request.session['errors']
        else:
            errors = {} #setting to none if no session errors exist
        manufacturers = models.Manufacturer().index()
        products = models.Product().index()
        context = {'manufacturers': manufacturers, 'products':products, 'errors':errors}
        return render(request, 'products/index.html', context)
    def post(self,request):
        errors = models.Product().create(request.POST)
        request.session['errors'] = errors
        return redirect('/products')
    def delete(self,request,id):
        models.delete(id)
        return redirect('/products')
class Edit(View):
    def get(self,request,id):
        # del request.session['errors']
        if request.session.get('errors'): #If session errors exist...
            errors = dict(request.session.get('errors')) #copying dict to 'error' so I can delete session error
            del request.session['errors']
        else:
            errors = {} #setting to none if no session errors exist
        manufacturers = models.Manufacturer().index()
        product = models.Product().show(id)
        context = {'product': product, 'manufacturers' : manufacturers, 'errors': errors}
        return render(request, 'products/edit.html', context)
    def post(self,request):
        errors = models.Product().update(request.POST)
        print "POST", request.POST
        print "ERRORS", errors
        if errors:
            request.session['errors'] = errors
            return redirect('/products/'+request.POST['id'])
        return redirect('/products')
