from rest_framework import serializers
from apis.models import Currency_convert

class CurrencyConvertSerializers(serializers.ModelSerializer):
    class Meta:
        model = Currency_convert
        fields = ('id','current_choice','amount','convert_choice')
               