# ecommerce_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Importa settings para arquivos de mídia
from django.conf.urls.static import static # Importa static para servir arquivos de mídia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')), # Inclui as URLs do app 'orders'
    path('', include('store.urls', namespace='store')), # Página Inicial (app 'store')
]

# Apenas para desenvolvimento: servir arquivos de mídia (sem JavaScript aqui)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)