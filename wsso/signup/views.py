from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .models import User
from importlib import import_module
from django.core.urlresolvers import clear_url_caches
from django.db import models
from django.apps import apps
from django.contrib import admin
from django.conf import settings
from signup.forms import *

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            userdetail=User.objects.create(
            Name=form.cleaned_data['Name'],
            Email=form.cleaned_data['Email'],
            Destrict=form.cleaned_data['District'],
            contact=form.cleaned_data['contact'],
                )
            return HttpResponseRedirect('frontend/index.html/')
    

    else:
        form = RegistrationForm()
    variables = {
    'form': form
    }

    
    return render(
    'signup/signup.html',
    variables,
    RequestContext(request)
    )

