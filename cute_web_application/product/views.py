from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
import os
# Create your views here.
def product(request):
    return HttpResponse("<h1>Вы в приложении product</h1>")

def product1(request):
    return render(request, 'site.html')