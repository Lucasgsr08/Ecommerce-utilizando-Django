# orders/urls.py

from django.urls import path
from . import views # Importa as views do seu próprio aplicativo 'orders'

app_name = 'orders' # Define o namespace para este app de URLs

urlpatterns = [
    # Exemplo: URL para criar um novo pedido
    path('create/', views.order_create, name='order_create'),
    # Adicione outras URLs relacionadas a pedidos aqui
]