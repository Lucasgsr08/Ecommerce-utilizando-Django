# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from store.models import Product
from .cart import Cart
from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    override_quantity = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

def cart_detail(request):
    """Exibe os detalhes do carrinho"""
    cart = Cart(request)
    # Adicionar formulário para cada item no carrinho
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override_quantity': True
        })
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def add_to_cart(request, product_id):
    """Adiciona produto ao carrinho"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            quantity = cd['quantity']
            override_quantity = cd['override_quantity']
            
            cart.add(product=product, quantity=quantity, override_quantity=override_quantity)
            
            if override_quantity:
                messages.success(request, f'Quantidade do {product.name} atualizada para {quantity}.')
            else:
                messages.success(request, f'{product.name} adicionado ao carrinho.')
            
            return redirect('cart:cart_detail')
    else:
        # Se for GET, adiciona 1 unidade do produto
        cart.add(product=product, quantity=1, override_quantity=False)
        messages.success(request, f'{product.name} adicionado ao carrinho.')
        return redirect('cart:cart_detail')

def remove_from_cart(request, product_id):
    """Remove produto do carrinho"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'{product.name} removido do carrinho.')
    return redirect('cart:cart_detail')