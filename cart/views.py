# cart/views.py

from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .cart import Cart
from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    override_quantity = forms.BooleanField(required=False, widget=forms.HiddenInput)

def cart_detail(request):
    cart = Cart(request)
    # AQUI É A MUDANÇA: Chame apenas 'cart_detail.html'.
    # O Django, com APP_DIRS=True, já sabe que este template pertence ao app 'cart'
    # e buscará dentro de 'cart/templates/cart_detail.html'
    # (ou em 'cart/templates/cart/cart_detail.html' dependendo de como o loader funciona internamente)
    # Teste primeiro com 'cart_detail.html'
    return render(request, 'cart_detail.html', {'cart': cart}) # <--- MUDANÇA AQUI!

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            override_quantity = form.cleaned_data['override_quantity']
            cart.add(product=product, quantity=quantity, override_quantity=override_quantity)
            return redirect('cart:cart_detail')
    else:
        return redirect('store:product_list')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')