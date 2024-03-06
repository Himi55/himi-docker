from django.db import models

# Create your models here.
VIDEO_CHOICES = (
    
    ("GIF","GIF"),
    ("AUDIO","AUDIO"),
    ("Image","Image"),
    
) 

class Video(models.Model):
    video   = models.FileField()
    VIDEO_CHOICES = models.CharField(max_length=100 ,choices=VIDEO_CHOICES)
    converted_video = models.FileField(null=True,blank=True) 