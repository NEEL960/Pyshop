from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})

# import products

# Create your views here.

# /products -->index
# Uniform Resource Locator (address)

# def index(request):
#     products=Product.object.all()
#     return HttpResponse("hello world ")
#
#
# def new(request):
#     return HttpResponse("New products")

