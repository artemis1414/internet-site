from django.shortcuts import render
from django.core.exceptions import ValidationError
from .forms import SignUpForm
from .models import User

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data_user = []
            for field in form.cleaned_data.values():
                data_user.append(field)
            print(form.cleaned_data)
            user = User.objects.create_user(data_user)
            user.save()
        else:
            data = {'form': form}
            return render(request, 'form_registration_alert.html', data)
    form = SignUpForm()
    data = {'form': form}
    return render(request, 'form_registration.html', data)

def sign_in(request):
    return render(request, 'core/form.html')
