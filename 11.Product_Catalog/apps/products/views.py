from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from django.views.generic import View
class index(View):
    def get(self,request):
        ''' method retrieving errors from messages
        errors = {}
        error_messages = messages.get_messages(request)
        for message in error_messages:
            errors[message.extra_tags] = str(message)
        if 'error' not in request.session:
            request.session['errors'] =''
        request.session['errors'] = {'test': 'something'}
        '''
        if request.session.get('errors'): #using session - If session errors exist...
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
        request.session['errors'] = errors #using session instead of messages to store error
        ''' method using messages to store errors
        if errors:
            for error in errors:
                messages.error(request, errors[error], extra_tags=error)
        '''
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
