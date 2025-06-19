# accounts/urls.py

from django.urls import path
from . import views # Corrigido: Importa views do seu próprio aplicativo 'accounts'
from django.contrib.auth import views as auth_views # Views padrão do Django para login/logout

app_name = 'accounts'

urlpatterns = [
    # Sua view personalizada de registro
    path('register/', views.register, name='register'),
    # Views de autenticação do Django, se você as estiver usando
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), # 'next_page' para redirecionar após logout
    # Adicione outras URLs do seu aplicativo 'accounts' aqui
]