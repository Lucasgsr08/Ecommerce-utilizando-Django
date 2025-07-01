# accounts/views.py
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .forms import SignUpForm   # ← agora importa o nome correto


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    next_page = '/'   # ou use o LOGOUT_REDIRECT_URL do settings


@login_required # Decorador para garantir que o usuário esteja logado
def profile(request):
    return render(request, 'accounts/profile.html')

def register(request):
    """
    Tela de cadastro + login automático após sucesso.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('store:product_list')   # ajuste se quiser
    else:
        form = SignUpForm()

    return render(request, 'registration/register.html', {'form': form})
