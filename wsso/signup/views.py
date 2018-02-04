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
'''
from signup.data.send_email import *
import urllib
from bs4 import BeautifulSoup
import signup.data'''

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            userdetail=UserDetails.objects.create(
            Name=form.cleaned_data['Name'],
            Email=form.cleaned_data['Email'],
            District=form.cleaned_data['District'],
            Block=form.cleaned_data['Block'],
            Panchayat=form.cleaned_data['Panchayat'],
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



'''
@background(schedule=60)
def email():
    data = []
    for i in range(8):
        page = open("signup/data/Contaminated("+str(i)+")")
        soup = BeautifulSoup(page, "lxml")
        table = soup.find_all("tr")
        rows = []
        for item in table:
            elements = []
            for ele in item.find_all("td"):
                elements.append(ele.text)
            rows.append(elements)
        data.append(rows)
    users = UserDetails.objects
    for district in data:
        for row in district:
            try:
                users_matched = users.filter(Panchayat=row[4])
            except:
                pass
            for u in users_matched:
                print('match found, sending email')
                send_email(u.Email, 'Contamination Alert', 'The contaminant in hazardous quantity is '+row[7]+'. The permissible limit is '+row[8]+' while the current value is '+row[9]+'. Please be safe.')
    return HttpResponseRedirect('/')
'''
