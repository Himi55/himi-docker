from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VideoConvertSerializers
from apis.models import VideoConvertModel
from rest_framework.schemas import AutoSchema
import coreapi
from rest_framework import generics
from rest_framework.exceptions import ParseError
from rest_framework.parsers import MultiPartParser,FormParser
import moviepy.editor as mp
from moviepy.editor import VideoFileClip
from moviepy.editor import *
import cv2
class VideoConvertView(generics.GenericAPIView):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = VideoConvertSerializers
    
    def post(self, request):
        serializer = VideoConvertSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
          

class VideoConvertGetData(APIView):
    def get(self, request, id=None):
        if id:
            item = VideoConvertModel.objects.get(id=id)
            if str(item.VIDEO_CHOICES) == "GIF":
             file = str(item.video.path)
             clip = VideoFileClip(file)
             clip.write_gif("mygif.gif",fps=1) # This line of code convert gif
        
            elif str(item.VIDEO_CHOICES) == "AUDIO":
                file = str(item.video.path)
                video = VideoFileClip(file)
                audio = video.audio                  # This line of code converting video file to audio file
                audio.write_audiofile("MyAudio.mp3") # This line of code for saving (.mp3) file
                # audio.save()

            elif str(item.VIDEO_CHOICES) == "Image":
                file = str(item.video.path)
                vidcap = cv2.VideoCapture(file)
                time_skips = float(12000)
                success,image = vidcap.read()
                count = 0
                while success:
                    # cv2.imshow("Output",image)     -----> this line of code to show video window on run time / but not working properly
                    cv2.imwrite("frame%d.jpg" % count, image)  # save image as jpg
                    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*time_skips)) 
                    # cv2.imshow("MYVIDEO.mp4",image)            
                    success,image = vidcap.read()
                    # print('Read a new frame: ', success)
                    count +=1
        items = VideoConvertModel.objects.all()
        serializer = VideoConvertSerializers(items, many=True)
        return Response({"status": "success",'id':item.id ,'video':item.video,'VIDEO CHOICE':item.VIDEO_CHOICES}, status=status.HTTP_200_OK)