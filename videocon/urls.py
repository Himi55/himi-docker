from django.contrib import admin
from django.urls import path 
from videocon import views

urlpatterns = [
    path('video/', views.index , name = 'videocon'),
    path('download1/<int:id>/',views.downloadfile , name = 'download1'),

]