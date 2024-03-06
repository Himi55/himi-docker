from django.contrib import admin
from django.urls import path
from currency import views 

urlpatterns = [
    path('convert/',views.currency_function , name = 'currency'),
]