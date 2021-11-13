from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from product.models import Product
from core.models import User
from .cart import Cart
from .models import CartItem
from .forms import CartAddProductForm


#@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        cart_base = CartItem(id_user=User.objects.get(id=request.user.id), products=cart.cart)
        cart_base.save()
    return redirect('/cart/')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    cart_base = CartItem(products=cart.cart)
    cart_base.save()
    return redirect('/cart/')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'detail.html', context={'cart': cart})
