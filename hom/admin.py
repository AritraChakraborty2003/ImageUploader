from django.contrib import admin
from .models import ImageDB
# Register your models here.
@admin.register(ImageDB)
class ImageDBAdmin(admin.ModelAdmin):
    list_display=['id','photo','time']