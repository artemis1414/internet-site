from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from .forms import SignUpForm
from .models import User

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data_user = form.cleaned_data
            user = User.objects.create_user(**data_user)
            user.save()
        else:
            data = {'form': form}
            return render(request, 'form_registration_alert.html', data)
    form = SignUpForm()
    data = {'form': form}
    return render(request, 'form_registration.html', data)

def sign_in(request):
    return render(request, 'core/form.html')

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'login_success.html')
    else:
        return render(request, 'registration/login.html')

def logout_user(request):
    logout(request)
    return render(request, 'registration/login.html')
