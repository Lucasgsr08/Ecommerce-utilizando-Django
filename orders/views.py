# orders/views.py

from django.shortcuts import render, redirect
from .models import Order, OrderItem # Importa Order e OrderItem
from .forms import OrderCreateForm # Importa o formulário que acabamos de criar
from cart.cart import Cart # Importa a classe Cart para acessar o carrinho

def order_create(request):
    cart = Cart(request) # Instancia o objeto do carrinho
    if not cart: # Se o carrinho estiver vazio, redireciona para a página do carrinho
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save() # Salva o pedido no banco de dados

            # Itera sobre os itens do carrinho e cria OrderItems
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'], # item['product'] já é o objeto Product
                    price=item['price'],
                    quantity=item['quantity']
                )
            # limpa o carrinho
            cart.clear()
            # Retorna para uma página de sucesso ou para a lista de produtos
            # Você precisará criar um template 'orders/order_created.html' para isso
            return render(request, 'orders/order_created.html', {'order': order})
        else:
            # Se o formulário não for válido, renderiza a página novamente com os erros
            return render(request, 'orders/order_create.html', {'cart': cart, 'form': form})
    else:
        form = OrderCreateForm() # Cria um formulário vazio para o método GET
    return render(request, 'orders/order_create.html', {'cart': cart, 'form': form})

# Você pode adicionar outras views para gerenciar pedidos aqui