from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Product, Category
import os
# Create your views here.
def product(request):
    list_category = Category.objects.all()
    return render(request, 'category.html', context={'category': list_category})

def detail(request, category_id, product_id):
    products_code = Product.objects.get(id=product_id)
    sizes_dict = Product.objects.filter(id=product_id).values()[0]
    sizes = []
    for i in range(36, 41):
        sizes.append((f'{i}', sizes_dict[f'size_{i}_value']))
    return render(request, 'product.html', context={'product': products_code, 'sizes': sizes, })

def catalog(request, category_id):
    print(category_id)
    list_product = Product.objects.filter(category_id=category_id)
    return render(request, 'product/product_base.html', context={'product': list_product})

