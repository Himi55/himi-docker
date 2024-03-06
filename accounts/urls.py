from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.home , name = 'home'),
    path('aboutus/',views.aboutus , name = 'aboutus'),
    path('create/',views.create_view, name = 'create'),
]