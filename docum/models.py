from django.db import models
import os

CONVERT_CHOICES = (
    ("pdf", "PDF"),
    ("docx", "DOCX"),
    ("html", "HTML"),
)



class UserFileUpload(models.Model):
   current_choices = models.CharField(max_length = 20,choices = CONVERT_CHOICES)
   file = models.FileField() 
   converted_file = models.FileField(null=True,blank=True) 
   convert_choices = models.CharField(max_length = 20,choices = CONVERT_CHOICES)
