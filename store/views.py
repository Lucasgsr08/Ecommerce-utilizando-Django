# Importações de módulos e classes necessários do Django e de outras bibliotecas
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.http import HttpResponseForbidden
from .models import Product, Category, Comment  # Importa os modelos do aplicativo atual
from .forms import CommentForm  # Importa o formulário de comentários do aplicativo atual

# Importações para a API REST (seção separada para clareza)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer, ProductSerializer  # Importa o serializer do aplicativo atual

# Importações para autenticação via token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer



# -----------------------------------------------------------------------------
# Views da Loja (Renderização de Páginas HTML)
# -----------------------------------------------------------------------------

def product_list(request, category_slug=None):
    """
    Lista produtos, com opções de filtragem por categoria, pesquisa e preço.
    Renderiza a página 'store/product/list.html'.
    """
    category = None
    # Obtém todas as categorias para exibir na sidebar/menu de filtros
    categories = Category.objects.all()
    # Inicia a query para produtos disponíveis
    products = Product.objects.filter(available=True)

    # Lógica para pesquisa de produtos pelo nome
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)  # Filtra produtos cujo nome contém a query

    # Lógica para filtrar produtos por categoria (se um slug de categoria for fornecido)
    if category_slug:
        # Obtém a categoria ou retorna 404 se não encontrada
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)  # Filtra produtos pela categoria selecionada

    # Lógica para filtrar produtos por faixa de preço
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)  # Preço maior ou igual ao mínimo
    if max_price:
        products = products.filter(price__lte=max_price)  # Preço menor ou igual ao máximo

    # Renderiza o template com os dados dos produtos e categorias
    return render(request, 'store/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })


def product_detail(request, id, slug):
    """
    Exibe os detalhes de um produto específico, incluindo seus comentários e formulário para novos comentários.
    Lida com a submissão de novos comentários.
    Renderiza a página 'store/product/detail.html'.
    """
    # Obtém o produto ou retorna 404 se não encontrado ou não disponível
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    # Obtém os comentários associados ao produto, otimizando a consulta com select_related('user')
    # e ordenando do mais recente para o mais antigo.
    comments = product.comments.select_related('user').order_by('-created_at')
    
    # Calcula a avaliação média e o total de avaliações para o produto
    rating_data = product.comments.aggregate(
        average_rating=Avg('rating'),  # Média do campo 'rating'
        total_reviews=Count('id')      # Contagem total de comentários
    )

    # Lógica para processar a submissão do formulário de comentário (requisição POST)
    if request.method == 'POST':
        if request.user.is_authenticated:  # Verifica se o usuário está logado
            form = CommentForm(request.POST)
            if form.is_valid():  # Valida os dados do formulário
                new_comment = form.save(commit=False)  # Cria uma instância do comentário, mas não salva ainda
                new_comment.product = product          # Associa o comentário ao produto
                new_comment.user = request.user        # Associa o comentário ao usuário logado
                new_comment.save()                     # Salva o comentário no banco de dados
                # Redireciona para a mesma página de detalhes do produto para evitar reenvio do formulário
                return redirect('store:product_detail', id=product.id, slug=product.slug)
            # Se o formulário não for válido, ele será renderizado novamente com os erros
        else:
            # Se o usuário não estiver autenticado e tentar postar, o formulário será inicializado vazio (ou pode-se redirecionar para login)
            form = CommentForm() # Isso pode ser omitido se a renderização for feita após o if/else
    else:
        # Para requisições GET (exibição inicial da página), inicializa um formulário vazio
        form = CommentForm()

    # Renderiza o template com os dados do produto, comentários, formulário e dados de avaliação
    return render(request, 'store/product/detail.html', {
        'product': product,
        'comments': comments,
        'form': form,
        'average_rating': rating_data['average_rating'],
        'total_reviews': rating_data['total_reviews'],
    })


@login_required  # Decorator que exige que o usuário esteja logado para acessar esta view
def edit_comment(request, pk):
    """
    Permite que um usuário edite seu próprio comentário.
    Verifica se o usuário logado é o autor do comentário.
    Renderiza a página 'store/comment_edit.html'.
    """
    # Obtém o comentário pelo ID ou retorna 404
    comment = get_object_or_404(Comment, pk=pk)
    
    # Verifica se o usuário logado é o autor do comentário.
    # Se não for, retorna um erro 403 (Forbidden).
    if comment.user != request.user:
        return HttpResponseForbidden("Você não pode editar este comentário.")

    # Lógica para processar a submissão do formulário de edição de comentário
    if request.method == 'POST':
        # Inicializa o formulário com os dados da requisição e a instância do comentário existente
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():  # Valida os dados
            form.save()      # Salva as alterações no comentário
            # Redireciona de volta para a página de detalhes do produto
            return redirect('store:product_detail', id=comment.product.id, slug=comment.product.slug)
    else:
        # Para requisições GET, inicializa o formulário com os dados atuais do comentário
        form = CommentForm(instance=comment)

    # Renderiza o template de edição com o formulário e o comentário
    return render(request, 'store/comment_edit.html', {
        'form': form,
        'comment': comment
    })


@login_required  # Decorator que exige que o usuário esteja logado para acessar esta view
def like_comment(request, pk):
    """
    Permite que um usuário dê 'like' ou 'deslike' em um comentário.
    Adiciona ou remove o usuário da lista de 'likes' do comentário.
    """
    # Obtém o comentário pelo ID ou retorna 404
    comment = get_object_or_404(Comment, pk=pk)
    user = request.user  # Obtém o usuário logado

    # Verifica se o usuário já deu 'like' no comentário
    if user in comment.likes.all():
        comment.likes.remove(user)  # Se já deu, remove o 'like'
    else:
        comment.likes.add(user)     # Se não deu, adiciona o 'like'
    
    # Redireciona de volta para a página de detalhes do produto
    return redirect('store:product_detail', id=comment.product.id, slug=comment.product.slug)


# -----------------------------------------------------------------------------
# Views de Páginas Estáticas/Informativas
# -----------------------------------------------------------------------------

def ajuda(request):
    """Renderiza a página de ajuda."""
    return render(request, 'store/ajuda.html')

def sobre(request):
    """Renderiza a página 'Sobre Nós'."""
    return render(request, 'store/sobre.html')

def contato(request):
    """Renderiza a página de contato."""
    return render(request, 'store/contato.html')


# -----------------------------------------------------------------------------
# Views da API REST (Endpoint para Dados JSON)
# -----------------------------------------------------------------------------

@api_view(['GET']) # Decorator que define que esta view aceita apenas requisições GET
def product_list_api(request):
    """
    Endpoint de API para listar todos os produtos.
    Retorna uma resposta JSON com os dados serializados dos produtos.
    """
    products = Product.objects.all()  # Obtém todos os produtos
    # Serializa os produtos (many=True indica que é uma coleção de objetos)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data) # Retorna os dados serializados como resposta JSON


# -----------------------------------------------------------------------------
# View de Detalhes do Produto na API REST
# -----------------------------------------------------------------------------
@api_view(['GET'])
def product_detail_api(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Produto não encontrado"}, status=404)

    serializer = ProductSerializer(product)
    return Response(serializer.data)


# -----------------------------------------------------------------------------
# View de Comentários do Produto na API REST
# -----------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def product_comments_api(request, pk):
    """
    GET → lista comentários de um produto
    POST → cria novo comentário se o usuário estiver logado
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Produto não encontrado"}, status=404)

    if request.method == 'GET':
        comments = product.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({"error": "Autenticação necessária para comentar."}, status=401)

        data = request.data.copy()
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user, product=product)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# -----------------------------------------------------------------------------
# View de Detalhes do Comentário na API REST
# -----------------------------------------------------------------------------
@api_view(['PUT', 'PATCH', 'DELETE'])
def comment_detail_api(request, comment_id):
    """
    PUT/PATCH → edita comentário (só se for o autor)
    DELETE → apaga comentário (só se for o autor)
    """
    try:
        comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        return Response({"error": "Comentário não encontrado"}, status=404)

    if request.user != comment.user:
        return Response({"error": "Você não tem permissão para modificar esse comentário."}, status=403)

    if request.method in ['PUT', 'PATCH']:
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        comment.delete()
        return Response({"message": "Comentário excluído com sucesso."}, status=204)

# -----------------------------------------------------------------------------
# View de Curtir/Descurtir Comentário na API REST
# -----------------------------------------------------------------------------
@api_view(['POST'])
def comment_like_toggle_api(request, comment_id):
    """
    POST → curte ou descurte comentário
    """
    if not request.user.is_authenticated:
        return Response({"error": "Autenticação necessária."}, status=401)

    try:
        comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        return Response({"error": "Comentário não encontrado"}, status=404)

    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
        return Response({"liked": False, "total_likes": comment.total_likes()})
    else:
        comment.likes.add(request.user)
        return Response({"liked": True, "total_likes": comment.total_likes()})
# -----------------------------------------------------------------------------
# View de Autenticação Personalizada (Token)
# -----------------------------------------------------------------------------


class CustomAuthToken(ObtainAuthToken):
    """
    POST: retorna o token de autenticação do usuário
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })