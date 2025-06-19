# cart/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from .cart import Cart # Importa a sua classe Cart do arquivo cart.py

# Função auxiliar para obter a instância do carrinho da sessão
def get_cart(request):
    """
    Retorna uma instância da classe Cart que gerencia o carrinho na sessão.
    """
    return Cart(request)

def cart_detail(request):
    """
    Exibe os detalhes do carrinho.
    """
    cart = get_cart(request) # Obtém a instância do carrinho
    return render(request, 'cart/detail.html', {'cart': cart})

@require_POST
def add_to_cart(request, product_id):
    """
    Adiciona um produto ao carrinho ou atualiza sua quantidade.
    """
    cart = get_cart(request) # Obtém a instância do carrinho
    product = get_object_or_404(Product, id=product_id)

    try:
        quantity = int(request.POST.get('quantity', 1))
    except ValueError:
        quantity = 1

    cart.add(product=product, quantity=quantity, override_quantity=False)

    return redirect('cart:cart_detail')

@require_POST
def remove_from_cart(request, item_id):
    """
    Remove um item do carrinho.
    """
    cart = get_cart(request)
    product = get_object_or_404(Product, id=item_id)

    cart.remove(product)

    return redirect('cart:cart_detail')