from rest_framework import serializers
from apis.models import VideoConvertModel 

class VideoConvertSerializers(serializers.ModelSerializer):
    class Meta:
        model = VideoConvertModel
        fields = ('id','video','VIDEO_CHOICES')
