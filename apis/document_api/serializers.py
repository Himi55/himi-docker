from rest_framework import serializers
from apis.models import UserFileUpload 

class DocumentConvertSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserFileUpload
        fields = ('id','current_choices','file','convert_choices')
