import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):

	Name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Name"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
	Email = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
	District = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("District"))
	Contact=forms.DecimalField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Contact"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })