from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CurrencyConvertSerializers
from apis.models import Currency_convert
from rest_framework.schemas import AutoSchema
import coreapi
from rest_framework import generics
from rest_framework.exceptions import ParseError
from rest_framework.parsers import MultiPartParser,FormParser

class CurrencyConvertView(generics.GenericAPIView):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = CurrencyConvertSerializers
    
    def post(self, request):
        serializer = CurrencyConvertSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success","data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CurrencyConvertGetData(APIView):
    def get(self, request, id=None):
        if id:
            item = Currency_convert.objects.get(id=id)
            if  str(item.current_choice) == "US Dollar":
                with open('api/api1.txt') as f:
                    lines = f.readlines()
                    currencyDict = {}
                    for line in lines:
                        parsed = line.split("\t")
                        currencyDict[parsed[0]] = parsed[1] 
                    if str(item.convert_choice):
                        result = item.amount * float(currencyDict[item.convert_choice])
                        
            elif  str(item.current_choice) == "Euro":
                with open('api/api2.txt') as f:
                    lines = f.readlines()
                    currencyDict = {}
                    for line in lines:
                        parsed = line.split("\t")
                        currencyDict[parsed[0]] = parsed[1] 
                    if str(item.convert_choice):
                        result = item.amount * float(currencyDict[item.convert_choice])
                        
            elif  str(item.current_choice) == "British Pound":
                with open('api/api3.txt') as f:
                    lines = f.readlines()
                    currencyDict = {}
                    for line in lines:
                        parsed = line.split("\t")
                        currencyDict[parsed[0]] = parsed[1] 
                    if str(item.convert_choice):
                        result = item.amount * float(currencyDict[item.convert_choice])
                        
            elif  str(item.current_choice) == "Australian Dollar":
                with open('api/api4.txt') as f:
                    lines = f.readlines()
                    currencyDict = {}
                    for line in lines:
                        parsed = line.split("\t")
                        currencyDict[parsed[0]] = parsed[1] 
                    if str(item.convert_choice):
                        result = item.amount * float(currencyDict[item.convert_choice])
                        
            elif  str(item.current_choice) == "Canadian Dollar":
                with open('api/api5.txt') as f:
                    lines = f.readlines()
                    currencyDict = {}
                    for line in lines:
                        parsed = line.split("\t")
                        currencyDict[parsed[0]] = parsed[1] 
                    if str(item.convert_choice):
                        result = item.amount * float(currencyDict[item.convert_choice])
                        
            elif  str(item.current_choice) == "Singapore Dollar":
                with open('api/api6.txt') as f:
                    lines = f.readlines()
                    currencyDict = {}
                    for line in lines:
                        parsed = line.split("\t")
                        currencyDict[parsed[0]] = parsed[1] 
                    if str(item.convert_choice):
                        result = item.amount * float(currencyDict[item.convert_choice])
            
            elif  str(item.current_choice) == "Swiss Franc":
                with open('api/api7.txt') as f:
                    lines = f.readlines()
                    currencyDict = {}
                    for line in lines:
                        parsed = line.split("\t")
                        currencyDict[parsed[0]] = parsed[1] 
                    if str(item.convert_choice):
                        result = item.amount * float(currencyDict[item.convert_choice])
                        
            elif  str(item.current_choice) == "Malaysian Ringgit":
                with open('api/api8.txt') as f:
                    lines = f.readlines()
                    currencyDict = {}
                    for line in lines:
                        parsed = line.split("\t")
                        currencyDict[parsed[0]] = parsed[1] 
                    if str(item.convert_choice):
                        result = item.amount * float(currencyDict[item.convert_choice])
            
            elif  str(item.current_choice) == "Japanese Yen":
                with open('api/api9.txt') as f:
                    lines = f.readlines()
                    currencyDict = {}
                    for line in lines:
                        parsed = line.split("\t")
                        currencyDict[parsed[0]] = parsed[1] 
                    if str(item.convert_choice):
                        result = item.amount * float(currencyDict[item.convert_choice])
                        
            elif  str(item.current_choice) == "Chinese Yuan Renminbi":
                with open('api/api10.txt') as f:
                    lines = f.readlines()
                    currencyDict = {}
                    for line in lines:
                        parsed = line.split("\t")
                        currencyDict[parsed[0]] = parsed[1] 
                    if str(item.convert_choice):
                        result = item.amount * float(currencyDict[item.convert_choice])
                        
            elif  str(item.current_choice) == "Indian Rupee":
                with open('api/api11.txt') as f:
                    lines = f.readlines()
                    currencyDict = {}
                    for line in lines:
                        parsed = line.split("\t")
                        currencyDict[parsed[0]] = parsed[1] 
                    if str(item.convert_choice):
                        result = item.amount * float(currencyDict[item.convert_choice])
                        
            return Response({"status": "success", "current_choice" : item.current_choice,"amount" : item.amount,"convert_choice" : item.convert_choice,"Result":result}, status=status.HTTP_200_OK)

        items = Currency_convert.objects.all()
        serializer = CurrencyConvertSerializers(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    