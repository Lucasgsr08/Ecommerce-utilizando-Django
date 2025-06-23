from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}! Você já pode fazer login.')
            return redirect('accounts:login')  # Certifique-se que você tem esta URL definida
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
