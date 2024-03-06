from django import forms
from docum.models import UserFileUpload

class UploadFileFormUser(forms.ModelForm):   
   class Meta:
      model = UserFileUpload
      fields = ['id','current_choices','file','convert_choices']
      
      