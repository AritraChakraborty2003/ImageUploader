from django.db import models

# Create your models here.
class ImageDB(models.Model):
    photo=models.FileField(upload_to="images",max_length=250,null=True,default=None)
    time=models.DateTimeField(auto_now_add=True)