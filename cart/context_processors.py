# cart/context_processors.py

from .cart import Cart # Importa a sua classe Cart

def cart(request):
    """
    Context processor para adicionar o objeto do carrinho
    ao contexto de todos os templates.
    """
    return {'cart': Cart(request)}