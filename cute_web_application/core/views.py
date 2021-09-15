from django.shortcuts import render
from django.core.exceptions import ValidationError
from .forms import SignUpForm
from .models import User

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form)
            user = User.objects.create_user(form.cleaned_data)
            user.save()
        else:
            data = {'form': form}
            return render(request, 'form_registration_alert.html', data)
    form = SignUpForm()
    data = {'form': form}
    return render(request, 'form_registration.html', data)

def sign_in(request):
    return render(request, 'core/form.html')
