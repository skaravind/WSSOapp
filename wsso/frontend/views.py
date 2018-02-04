from django.shortcuts import render
from signup.tasks import *
# Create your views here.

def index(request):
	email()
	return render(request, 'frontend/index.html')
