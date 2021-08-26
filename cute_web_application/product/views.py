from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Product
import os
# Create your views here.
def product(request):
    return render(request, 'product/product_base.html')

def detail(request, product_id):
    products_code = Product.objects.get(id=product_id)
    return render(request, 'product.html', context={'product': products_code})
