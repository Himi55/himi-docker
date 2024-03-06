from django import forms
from .models import Currency_convert_model

class Currency_form(forms.ModelForm):
  class Meta:
    model = Currency_convert_model
    fields = '__all__'