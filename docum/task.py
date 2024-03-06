from __future__ import absolute_import
from celery import shared_task
import django.contrib
from time import sleep
from docum.utils import document_convert_celery_task
from celery import  shared_task, Celery 
from time import sleep
from celery_progress.backend import ProgressRecorder
# app = Celery('task', backend='redis', broker='redis://localhost:6379')

@shared_task(bind=True)
def go_to_sleep(self, duration):
  progress_recorder = ProgressRecorder(self)
  result =0
  for i in range(100):
    sleep(duration)
    result +=1
    progress_recorder.set_progress(i + 1, duration)
    #sleep(duration)
    return result


@shared_task
def sleepy(duration):
  sleep(duration)
  return None

@shared_task
def document_converter_celery_task_function(form_current_choices,form_file_data,form_convert_choices,instance_id):
  document_convert_celery_task(form_current_choices,form_file_data,form_convert_choices,instance_id)
  return None



from celery.signals import task_postrun
@task_postrun.connect(retry=True)
def task_postrun_handler(**kwargs):
    if kwargs.pop('state') == 'IGNORED':
        task = kwargs.pop('task')
        task.update_state(state='IGNORED', meta=str(kwargs.pop('retval')))