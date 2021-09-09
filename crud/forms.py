from django import forms
from django import *


class Form(forms.Form):
    key_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    key_description = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
