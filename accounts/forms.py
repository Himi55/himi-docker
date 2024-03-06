from django import forms  
from .models import UserContactDetails ,UserRegisterModel

class UserContactRegistration(forms.ModelForm):
  class Meta:
    model = UserContactDetails
    fields = '__all__'


class UserContactRegistration(forms.ModelForm):
  class Meta:
    model = UserContactDetails
    fields = '__all__'