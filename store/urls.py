from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    
        # Novas rotas
    path('contato/', views.contato, name='contato'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('sobre/', views.sobre, name='sobre'),
    
    
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]
