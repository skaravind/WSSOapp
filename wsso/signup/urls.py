from django.conf.urls import url
from . import views

# Create your views here.
urlpatterns = [
	url(r'^$', views.register, name = 'signup')
]
