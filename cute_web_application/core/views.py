from django.shortcuts import render

# Create your views here.

def registration(request):
    return render(request, 'form_registration.html')

def signinsystem(request):
    return render(request, 'core/form.html')
