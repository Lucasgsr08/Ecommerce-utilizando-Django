from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.http import HttpResponseForbidden
from .models import Product, Category, Comment
from .forms import CommentForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

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
    comments = product.comments.select_related('user').order_by('-created_at')
    rating_data = product.comments.aggregate(
        average_rating=Avg('rating'),
        total_reviews=Count('id')
    )

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.product = product
                new_comment.user = request.user
                new_comment.save()
                return redirect('store:product_detail', id=product.id, slug=product.slug)
        else:
            form = CommentForm()
    else:
        form = CommentForm()

    return render(request, 'store/product/detail.html', {
        'product': product,
        'comments': comments,
        'form': form,
        'average_rating': rating_data['average_rating'],
        'total_reviews': rating_data['total_reviews'],
    })

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user != request.user:
        return HttpResponseForbidden("Você não pode editar este comentário.")

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('store:product_detail', id=comment.product.id, slug=comment.product.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'store/comment_edit.html', {
        'form': form,
        'comment': comment
    })

@login_required
def like_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    user = request.user
    if user in comment.likes.all():
        comment.likes.remove(user)
    else:
        comment.likes.add(user)
    return redirect('store:product_detail', id=comment.product.id, slug=comment.product.slug)

def ajuda(request):
    return render(request, 'store/ajuda.html')

def sobre(request):
    return render(request, 'store/sobre.html')

def contato(request):
    return render(request, 'store/contato.html')
