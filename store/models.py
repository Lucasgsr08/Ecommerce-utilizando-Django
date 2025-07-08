# store/models.py

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# ================================
# 📦 Model: Categoria de Produto
# ================================
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)  # Nome da categoria
    slug = models.SlugField(max_length=200, unique=True)    # Slug para URL amigável

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Retorna a URL da listagem de produtos da categoria
        return reverse('store:product_list_by_category', args=[self.slug])


# ================================
# 🛍️ Model: Produto
# ================================
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)  # Categoria associada
    name = models.CharField(max_length=200, db_index=True)  # Nome do produto
    slug = models.SlugField(max_length=200, db_index=True)  # Slug para URL amigável
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)  # Imagem do produto
    description = models.TextField(blank=True)  # Descrição
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço
    available = models.BooleanField(default=True)  # Produto disponível?
    created = models.DateTimeField(auto_now_add=True)  # Criado em
    updated = models.DateTimeField(auto_now=True)      # Atualizado em

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Retorna a URL da página de detalhes do produto
        return reverse('store:product_detail', args=[self.id, self.slug])


# ===========================================
# 💬 Model: Comentários e Avaliações
# ===========================================
class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)  # Produto comentado
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Autor do comentário
    text = models.TextField("Comentário")  # Texto do comentário
    rating = models.IntegerField(  # Avaliação de 1 a 5 estrelas
        "Avaliação (1 a 5)",
        choices=[(i, i) for i in range(1, 6)],
        default=5
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Criado em
    updated_at = models.DateTimeField(auto_now=True)      # Atualizado em (se editado)
    likes = models.ManyToManyField(  # Likes de outros usuários
        User,
        related_name='liked_comments',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.rating} estrela(s)'

    def total_likes(self):
        # Retorna o total de likes no comentário
        return self.likes.count()
