from django.db import models

# Create Models here.

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

class Currency_convert_model(models.Model):
  current_choice = models.CharField(max_length = 50 , choices= CONVERT_CHOICES)
  amount = models.IntegerField()
  convert_choice = models.CharField(max_length = 50 , choices= CONVERT_CHOICES)
  