# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
# from .forms import UserRegisterForm # Descomente e garanta que você tem este formulário

def register(request):
    """
    View para registro de novos usuários.
    """
    if request.method == 'POST':
        # form = UserRegisterForm(request.POST) # Descomente e use seu formulário aqui
        # if form.is_valid():
        #     user = form.save()
        #     messages.success(request, 'Sua conta foi criada com sucesso! Você pode agora fazer login.')
        #     auth_login(request, user) # Faz o login automático após o registro
        #     return redirect('store:product_list') # Redireciona para a página inicial da loja
        # else:
        #     messages.error(request, 'Ocorreu um erro durante o registro. Por favor, corrija os erros abaixo.')
        # Código temporário para simular o registro se o formulário não estiver implementado:
        messages.success(request, 'Registro simulado com sucesso!')
        return redirect('store:product_list')
    else:
        # form = UserRegisterForm() # Descomente e use seu formulário aqui
        pass # Apenas um pass para evitar erro de sintaxe temporariamente

    # return render(request, 'accounts/register.html', {'form': form}) # Descomente quando o formulário estiver pronto
    return render(request, 'accounts/register.html', {}) # Retorna sem form por enquanto se não estiver pronto

# Outras views de accounts (se houverem) viriam aqui
# Exemplo de login (se você tiver uma view personalizada em vez de usar auth_views.LoginView)
# def user_login(request):
#     # Sua lógica de login
#     pass