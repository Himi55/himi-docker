# Convert PDF file To Document File Code
from pdf2docx import parse
import aspose.words as aw
from htmldocx import HtmlToDocx
import pdfkit
import os 
from django.conf import settings
from docum.models import UserFileUpload

def document_convert_celery_task(form_current_choices,form_file_data,form_convert_choices,instance_id):
    if str(form_current_choices) == "pdf":
        if str(form_convert_choices) == "docx":
            pdf_file = str(form_file_data)
            word_path = "media/test.docx"
            word_file = "test.docx"
            parse(pdf_file, word_path, start=0, end=None) 
            instance = UserFileUpload.objects.get(id=instance_id)
            instance.converted_file = word_file
            instance.save()
    # End Code PDF file To Document File 
    
    # Convert Document To HTML File Code 
    
    elif str(form_current_choices) == "docx":
        if str(form_convert_choices) == "html":
            docx_file = str(form_file_data)
            doc = aw.Document(docx_file)
            saveOptions = aw.saving.HtmlSaveOptions()
            saveOptions.export_roundtrip_information = True
            word_path = "media/Document.html"
            word_file = "Document.html"
            doc.save(word_path, saveOptions)
            instance = UserFileUpload.objects.get(id=instance_id)
            instance.converted_file = word_file
            instance.save()
    # End Code Convert Document to HTML file 
    
    # Convert HTML to Doxc File Code
    
    elif str(form_current_choices) == "html":
        if str(form_convert_choices) == "docx":
            html_file = str(form_file_data)
            new_parser = HtmlToDocx()
            word_path = "media/index.docx"
            word_file = "index.docx"
            new_parser.parse_html_file(html_file, word_path)
            instance = UserFileUpload.objects.get(id=instance_id)
            instance.converted_file = word_file
            instance.save()
    # End Code Convert HTML to Document file 
    
    # Convert PDF to HTML  Code
    
    elif str(form_current_choices) == "pdf":
        if str(form_convert_choices) == "html":
            pdf_file = str(form_file_data)
            doc = aw.Document(pdf_file)
            word_path = "media/Output.html"
            word_file = "Output.html"
            doc.save(word_file)
            instance = UserFileUpload.objects.get(id=instance_id)
            instance.converted_file = word_file
            instance.save()
    # End Code Convert PDF to HTML file
    else:
        if str(form_current_choices) == "html":
            if str(form_convert_choices) == "pdf":
                html_file = str(form_file_data) 
                word_path = "media/out.pdf"
                word_file = "out.pdf"
                pdfkit.from_file(html_file,word_path)
                instance = UserFileUpload.objects.get(id=instance_id)
                instance.converted_file = word_file
                instance.save()