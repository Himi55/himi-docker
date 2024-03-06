from django.shortcuts import render
from .models import Currency_convert_model
from .forms import Currency_form
from django.http import HttpResponse

def currency_function(request):
  if request.method == 'POST':
    form = Currency_form(request.POST)
    if form.is_valid():
      current_choice = form.cleaned_data['current_choice']
      enter_amount = form.cleaned_data['amount']
      enter_choice = form.cleaned_data['convert_choice']
      if  str(current_choice) == "US Dollar":
          with open('api/api1.txt') as f: 
              lines = f.readlines()
              currencyDict = {}
              for line in lines:
                  parsed = line.split("\t")
                  currencyDict[parsed[0]] = parsed[1] 
              if str(enter_choice):
                form = Currency_form()  
                convert_amount = enter_amount * float(currencyDict[enter_choice]) 
            
      elif  str(current_choice) == "Euro":
          with open('api/api2.txt') as f:
              lines = f.readlines()
              currencyDict = {}
              for line in lines:
                  parsed = line.split("\t")
                  currencyDict[parsed[0]] = parsed[1] 
              if str(enter_choice):  
                form = Currency_form()
                convert_amount = enter_amount * float(currencyDict[enter_choice])

      elif  str(current_choice) == "British Pound":
          with open('api/api3.txt') as f:
              lines = f.readlines()
              currencyDict = {}
              for line in lines:
                  parsed = line.split("\t")
                  currencyDict[parsed[0]] = parsed[1] 
              if str(enter_choice):  
                form = Currency_form()
                convert_amount = enter_amount * float(currencyDict[enter_choice])

      elif  str(current_choice) == "Australian Dollar":
          with open('api/api4.txt') as f:
              lines = f.readlines()
              currencyDict = {}
              for line in lines:
                  parsed = line.split("\t")
                  currencyDict[parsed[0]] = parsed[1] 
              if str(enter_choice):  
                form = Currency_form()
                convert_amount = enter_amount * float(currencyDict[enter_choice])
       
      elif  str(current_choice) == "Canadian Dollar":
          with open('api/api5.txt') as f:
              lines = f.readlines()
              currencyDict = {}
              for line in lines:
                  parsed = line.split("\t")
                  currencyDict[parsed[0]] = parsed[1] 
              if str(enter_choice):  
                form = Currency_form()
                convert_amount = enter_amount * float(currencyDict[enter_choice])
              
      elif  str(current_choice) == "Singapore Dollar":
          with open('api/api6.txt') as f:
              lines = f.readlines()
              currencyDict = {}
              for line in lines:
                  parsed = line.split("\t")
                  currencyDict[parsed[0]] = parsed[1] 
              if str(enter_choice):  
                form = Currency_form()
                convert_amount = enter_amount * float(currencyDict[enter_choice])
            
      elif  str(current_choice) == "Swiss Franc":
          with open('api/api7.txt') as f:
              lines = f.readlines()
              currencyDict = {}
              for line in lines:
                  parsed = line.split("\t")
                  currencyDict[parsed[0]] = parsed[1] 
              if str(enter_choice):  
                form = Currency_form()
                convert_amount = enter_amount * float(currencyDict[enter_choice])
              
      elif  str(current_choice) == "Malaysian Ringgit":
          with open('api/api8.txt') as f:
              lines = f.readlines()
              currencyDict = {}
              for line in lines:
                  parsed = line.split("\t")
                  currencyDict[parsed[0]] = parsed[1] 
              if str(enter_choice):  
                form = Currency_form()
                convert_amount = enter_amount * float(currencyDict[enter_choice])
              
      elif  str(current_choice) == "Japanese Yen":
          with open('api/api9.txt') as f:
              lines = f.readlines()
              currencyDict = {}
              for line in lines:
                  parsed = line.split("\t")
                  currencyDict[parsed[0]] = parsed[1] 
              if str(enter_choice):  
                form = Currency_form()
                convert_amount = enter_amount * float(currencyDict[enter_choice])
              
      elif  str(current_choice) == "Chinese Yuan Renminbi":
          with open('api/api10.txt') as f:
              lines = f.readlines()
              currencyDict = {}
              for line in lines:
                  parsed = line.split("\t")
                  currencyDict[parsed[0]] = parsed[1] 
              if str(enter_choice):  
                form = Currency_form()
                convert_amount = enter_amount * float(currencyDict[enter_choice])
              
      elif  str(current_choice) == "Indian Rupee":
          with open('api/api11.txt') as f:
              lines = f.readlines()
              currencyDict = {}
              for line in lines:
                  parsed = line.split("\t")
                  currencyDict[parsed[0]] = parsed[1] 
              if str(enter_choice):  
                form = Currency_form()
                convert_amount = enter_amount * float(currencyDict[enter_choice])
      return render(request,"currversion.html",{'form':form,'key':convert_amount}) 
  else:
    form = Currency_form()
  return render(request,"currversion.html",{'form':form})  
  