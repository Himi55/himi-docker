import moviepy.editor as mp
from moviepy.editor import VideoFileClip
from moviepy.editor import *
# import cv2  
from videocon.models import Video


def send_admin_mail(form_file_data,form_choice_data,instance_id):
  if str(form_choice_data) == "GIF":
            file = str(form_file_data)
            clip = VideoFileClip(file)
            clip = clip.subclip(0,4)
            word_path = "media/mygif.gif"
            word_file = "mygif.gif"
            clip.write_gif(word_path,fps=7) # This line of code convert gif
            instance = Video.objects.get(id=instance_id)
            instance.converted_video = word_file
            instance.save()
        
  elif str(form_choice_data) == "AUDIO":
      file = str(form_file_data)
      video = VideoFileClip(file)
      audio = video.audio    
      word_path = "media/MyAudio.mp3"
      word_file = "MyAudio.mp3"              
      audio.write_audiofile(word_path)
      instance = Video.objects.get(id=instance_id)
      instance.converted_video = word_file
      instance.save()
      # audio.save()

#   elif str(form_choice_data) == "Image":
#       file = str(form_file_data)
#       vidcap = cv2.VideoCapture(file)
#       time_skips = float(12000)
#       success,image = vidcap.read()
#       count = 0
#       while success:
#           cv2.imwrite("frame%d.jpg" % count, image)  # save image as jpg
#           vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*time_skips))          
#           success,image = vidcap.read()
#           count +=1