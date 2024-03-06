import re
from django.shortcuts import redirect, render
from videocon.models import Video
from django.http import HttpResponse, HttpResponseRedirect
from videocon.forms import Video_form
import os
import time
from videocon.tasks import VideoFunction
# Create your views here.

# Code of  convert mp4 to Gif ------------------->>     
def index(request):
    if request.method =='POST':
        form = Video_form(request.POST, request.FILES)
        if form.is_valid():
            form_file_data = form.cleaned_data['video']
            form_choice_data = form.cleaned_data['VIDEO_CHOICES']
            form_file_data = str(form_file_data)
            form_choice_data = str(form_choice_data)
            fm=form.save()
            instance_id =fm.id
            result = VideoFunction.delay(form_file_data,form_choice_data,instance_id)
            print(result)
            while result.status != 'SUCCESS':
                time.sleep(3)
            return redirect(f'/videocon/download1/{instance_id}')
    else:
        form = Video_form()
    return render(request,"videocon.html",{'form':form})


def downloadfile(request,id):
    userfiledownload = Video.objects.get(id=id)
    return render(request,'download1.html',{'download1':userfiledownload})