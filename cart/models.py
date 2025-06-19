from django.db import models
from django.contrib.auth.models import User
from store.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        """Calcula o preço total de todos os itens no carrinho"""
        return sum(item.get_total_price() for item in self.items.all())

    def get_total_items(self):
        """Calcula o número total de itens no carrinho"""
        return sum(item.quantity for item in self.items.all())

    def __str__(self):
        return f"Carrinho do usuário: {self.user.username if self.user else 'Anônimo'}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        """Calcula o preço total deste item (preço * quantidade)"""
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    class Meta:
        unique_together = ('cart', 'product')