# from celery import shared_task
# import django.contrib
# from time import sleep
# from accounts.utils import Mailer

# @shared_task
# def sleepy(duration):
#   sleep(duration)
#   return None

# @shared_task
# def send_mail_user_task(recepient,subject,message):
#   Mailer.send_user_mail(recepient,subject,message)
#   Mailer.send_admin_mail(recepient)
#   return None