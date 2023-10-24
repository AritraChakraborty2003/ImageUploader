from django.shortcuts import render
from hom import models
from hom.models import ImageDB
from .forms import ImageForm
from django.contrib import messages
# Create your views here.
def index(request):
    form=ImageForm(request.POST,request.FILES)
    if form.is_valid():
        messages.success(request, "Image uploaded successfully...")
        form.save()
    form=ImageForm()
    img=ImageDB.objects.all()
    return render(request,"index.html",{'form':form,'img':img})