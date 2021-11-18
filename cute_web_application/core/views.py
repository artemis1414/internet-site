import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, UpdateProfile
from .models import User
from cart.models import Order
from product.models import Product
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data_user = form.cleaned_data
            if User.objects.filter(username=data_user['username']).exists():
                data = {'form': form}
                return render(request, 'form_registration_alert.html', data)
            user = User.objects.create_user(**data_user)
            user.save()
            return render(request, 'form_complete.html')
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

def sell_history(request):
    sell_base = Order.objects.filter(id_user=request.user.id)
    if sell_base:
        sell = Order.objects.filter(id_user=request.user.id)
    else:
        sell = None
    return render(request, 'sell_history.html', context={'sell': sell})

def detail_order(request, order_id):
    order = Order.objects.get(id=order_id)
    cart = json.loads(order.structure)
    products = Product.objects.filter(id__in=cart.keys())
    for product in products:
        product.value = cart[str(product.id)]['quantity']
    cart['cost'] = order.cost
    return render(request, 'detail_order.html', context={'order': order, 'products': products, 'cart': cart})

def update_profile(request):
    user = User.objects.get(id=request.user.id)
    form = UpdateProfile()
    if request.method == "POST":
        form = UpdateProfile(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            user.first_name = data_form['first_name']
            user.last_name = data_form['last_name']
            user.phone = data_form['phone']
            user.save()
            return render(request, 'update_complete.html')
    context = {'form': form}
    return render(request, 'update_profile.html', context=context)

