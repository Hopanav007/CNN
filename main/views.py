import os
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest
from django.shortcuts import render
from imageClassifier import settings
from .models import Image
from . import test


def insert_items(request: HttpRequest):
    if request.method == 'POST':
        f = request.FILES['file']
        fs = FileSystemStorage()
        file = fs.save(str(f), f)
        fileurl = fs.url(file)
        classification = test.prediction(os.path.join(settings.MEDIA_ROOT, file))
        image = Image(base64Image=fileurl, image_class=classification)
        context = {"url": fileurl, "title": classification}
        image.save()
        return render(request,'main/image_form.html',context)
    else:
        return render(request, 'main/image_form.html')
