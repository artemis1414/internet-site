from django.shortcuts import render
from django.core.exceptions import ValidationError
from .forms import SignUpForm

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            pass
        else:
            return ValidationError
    form = SignUpForm()
    data = {'form': form}
    return render(request, 'form_registration.html', data)

def sign_in(request):
    return render(request, 'core/form.html')
