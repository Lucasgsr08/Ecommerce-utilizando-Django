from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('pagamento/<int:order_id>/', views.payment_simulation, name='payment_simulation'),
    path('pagamento/sucesso/', views.order_success, name='order_success'),
]
