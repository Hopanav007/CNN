import base64
from django.db import models  

class Image(models.Model):  
    base64Image = models.TextField()  
    image_class = models.CharField(max_length=200)  
