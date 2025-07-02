from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# Criação de pedido + redirecionamento para pagamento simulado
def order_create(request):
    cart = Cart(request)
    if not cart:
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            cart.clear()
            return redirect('orders:payment_simulation', order_id=order.id)
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order_create.html', {'cart': cart, 'form': form})

# Página que simula o redirecionamento para Stripe
def payment_simulation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/payment_simulation.html', {'order': order})

# Página de sucesso que marca o pedido como "pago"
def order_success(request):
    order_id = request.GET.get('order_id')
    if order_id:
        order = Order.objects.get(id=order_id)
        order.paid = True
        order.status_pagamento = 'pago'
        order.save()
    return render(request, 'orders/order_created.html', {'order': order})
