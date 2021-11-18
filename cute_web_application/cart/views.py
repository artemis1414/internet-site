from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from product.models import Product
from core.models import User
from .cart import Cart
from .models import CartItem, Order
from .forms import CartAddProductForm, AddOrder
import json

def cart_exist(request):
    cart_user = CartItem.objects.filter(id_user=request.user.id)
    if len(cart_user) != 1:
        cart = {}
        products = json.dumps(cart)
        cart_base = CartItem(id_user=User.objects.get(id=request.user.id), products=products)
        cart_base.save()
    return True

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    if request.user.is_authenticated:
        cart_exist(request)
        cart_base = CartItem.objects.get(id_user=request.user.id)
        cart.cart = json.loads(cart_base.products)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        if request.user.is_authenticated:
            cart_exist(request)
            cart_base = CartItem.objects.get(id_user=request.user.id)
            cart_base.products = json.dumps(cart.cart)
            cart_base.save()
    return redirect('/cart/')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        cart_base = CartItem.objects.get(id_user=request.user.id)
        cart.cart = json.loads(cart_base.products)
        cart.remove(product)
        cart_base.products = json.dumps(cart.cart)
        cart_base.save()
    else:
        cart.remove(product)
    return redirect('/cart/')

def cart_detail(request):
    if request.user.is_authenticated:
        cart_exist(request)
        cart_base = CartItem.objects.get(id_user=request.user.id)
        cart = Cart(request)
        cart.cart = json.loads(cart_base.products)
    else:
        cart = Cart(request)
    return render(request, 'detail.html', context={'cart': cart})

def dec_order(request):
    if request.method == 'POST':
        cart = Cart(request)
        form = AddOrder(request.POST)
        if form.is_valid():
            order_data = form.cleaned_data
            name_and_phone = order_data['name'] + ' ' + str(order_data['phone'])
            if request.user.is_authenticated:
                order = Order(id_user=User.objects.get(id=request.user.id),
                              name_and_phone=name_and_phone,
                              structure=json.dumps(cart.cart),
                              cost=cart.get_total_price(),
                              address=order_data['address'])
                order.save()
                cart_base = CartItem.objects.get(id_user=request.user.id)
                cart.cart = {}
                cart_base.products = json.dumps(cart.cart)
                cart_base.save()
            else:
                order = Order(name_and_phone=name_and_phone,
                              structure=json.dumps(cart.cart),
                              cost=cart.get_total_price(),
                              address=order_data['address'])
                order.save()
                cart.cart = {}
            return render(request, 'order_complete.html', context={'order': order})
        else:
            return render(request, 'order_alert.html', context={'form': form})
    form = AddOrder()
    cart = Cart(request)
    return render(request, 'order.html', context={'form': form, 'cart': cart})



