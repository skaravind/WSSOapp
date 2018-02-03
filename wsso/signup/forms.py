import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):

	Name = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Name"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
	email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
	District = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("District"))
	contact=forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Contact"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })

