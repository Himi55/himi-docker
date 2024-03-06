from django.db import models

CONVERT_CHOICES = (
    ("US Dollar", "USD"),
    ("Euro", "EURO"),
    ("British Pound","ASTRLN"),
    ("Australian Dollar","BRTSH"),
    ("Canadian Dollar", "CNDN"),
    ("Singapore Dollar", "SNGPR"),
    ("Swiss Franc", "SWSFRNC"),
    ("Malaysian Ringgit","MLYSN"),
    ("Japanese Yen","JPNS"),
    ("Chinese Yuan Renminbi","CHNS"),
    ("Indian Rupee","INR"),
) 


class Currency_convert(models.Model):
    current_choice = models.CharField(max_length = 50 , choices= CONVERT_CHOICES)
    amount = models.IntegerField()
    convert_choice = models.CharField(max_length = 50 , choices= CONVERT_CHOICES)
    result = models.IntegerField(null=True)
    
    


CONVERT_CHOICES = (
    ("pdf", "PDF"),
    ("docx", "DOCX"),
    ("html", "HTML"),
)

class UserFileUpload(models.Model):
   current_choices = models.CharField(max_length = 20,choices = CONVERT_CHOICES)
   file = models.FileField() 
   convert_choices = models.CharField(max_length = 20,choices = CONVERT_CHOICES)
   
   

VIDEO_CHOICES = (
    
    ("GIF","GIF"),
    ("AUDIO","AUDIO"),
    ("Image","Image"),
    
) 

class VideoConvertModel(models.Model):
    video   = models.FileField(upload_to="video/%y")
    VIDEO_CHOICES = models.CharField(max_length=100 ,choices=VIDEO_CHOICES)
    