from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .models import UserDetails
from importlib import import_module
from django.urls import clear_url_caches
from django.db import models
from django.apps import apps
from django.contrib import admin
from django.conf import settings
from signup.forms import *

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            userdetail=UserDetails.objects.create(
            Name=form.cleaned_data['Name'],
            Email=form.cleaned_data['Email'],
            District=form.cleaned_data['District'],
            Contact=form.cleaned_data['Contact'],
                )
            return HttpResponseRedirect('/')
    

    else:
        form = RegistrationForm()
    variables = {
    'form': form
    }

    
    return render_to_response(
    'signup/signup.html',
    variables,
    )

