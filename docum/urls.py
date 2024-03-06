from django.contrib import admin
from django.urls import path
from docum import views

app_name="docum"

urlpatterns = [
    path('docversion/',views.docx2pdf_converter, name = 'docversion'),
    # path('rom/<uuid:task_id>',views.get_progress , name = 'task_status'),
    path('download/<int:id>/',views.downloadfile , name = 'download'),
]