# ecommerce/store/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Comment
from .forms import CommentForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    # Filtro por nome (busca)
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    # Filtro por categoria
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Filtro por preço
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    return render(request, 'store/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    comments = product.comments.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.product = product
                new_comment.user = request.user
                new_comment.save()
                form = CommentForm()  # limpa o formulário
        else:
            form = CommentForm()  # usuário não autenticado
    else:
        form = CommentForm()

    return render(request, 'store/product/detail.html', {
        'product': product,
        'comments': comments,
        'form': form
    })


def ajuda(request):
    return render(request, 'store/ajuda.html')

def sobre(request):
    return render(request, 'store/sobre.html')

def contato(request):
    return render(request, 'store/contato.html')
