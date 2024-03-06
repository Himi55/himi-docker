from celery import shared_task
import django.contrib
from time import sleep
from videocon.utils import send_admin_mail


@shared_task
def sleepy(duration):
  sleep(duration)
  return None


@shared_task
def VideoFunction(form_file_data,form_choice_data,instance_id):
  send_admin_mail(form_file_data,form_choice_data,instance_id)
  return None