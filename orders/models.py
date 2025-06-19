# orders/models.py

from django.db import models
from store.models import Product # Importa o modelo Product de store

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created'] # Ordena os pedidos por data de criação decrescente

    def __str__(self):
        return f'Order {self.id}' # String de representação do objeto Order

    def get_total_cost(self):
        # Calcula o custo total do pedido somando os custos de todos os itens do pedido
        return sum(item.get_cost() for item in self.items.all()) # Assume que 'self.items' é o related_name de OrderItem

class OrderItem(models.Model):
    # Corrigido: ForeignKey deve apontar para o modelo 'Order' diretamente.
    # Se 'Order' estiver definido ANTES de 'OrderItem' no mesmo arquivo, pode-se usar o nome da classe.
    # Caso contrário, é mais seguro usar o nome do modelo como string ('orders.Order')
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity