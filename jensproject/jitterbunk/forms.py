from django import forms
from .models import Bunkform

from django.forms import ModelForm


class BunkForm(forms.Form):
    bunker = forms.CharField(label="Your username", max_length=200)
    bunked = forms.CharField(label="Their username", max_length=200)