# listing/forms.py

from django import forms
from .models import Product

class producAddForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ["name", "date_in",]
    labels = {'name': "Name", "date_in": "date",}