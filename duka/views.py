from django.shortcuts import render

# Create your views here.

from .models import Products

def index(request):
    product_objects = Products.objects.all()
    return render(request,'duka/index.html',{'product_objects':product_objects})