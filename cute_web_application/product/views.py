from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
import os
# Create your views here.
def product(request):
    return HttpResponse("<h1>Вы в приложении product</h1>")

def product1(request):
    with open('product\\templates\\1\\site.html', encoding='UTF-8') as f:
        html = f.read()
        return HttpResponse(html)