from django.urls import path
from . import views
from .views import CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'store'

urlpatterns = [
    path('contato/', views.contato, name='contato'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('sobre/', views.sobre, name='sobre'),
    path('comentario/<int:pk>/editar/', views.edit_comment, name='edit_comment'),
    path('comentario/<int:pk>/curtir/', views.like_comment, name='like_comment'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('api/products/', views.product_list_api, name='product_list_api'),
    path('api/products/<int:pk>/', views.product_detail_api, name='product_detail_api'),
    path('api/products/<int:pk>/comments/', views.product_comments_api, name='product_comments_api'),
    path('api/comments/<int:comment_id>/', views.comment_detail_api, name='comment_detail_api'),
    path('api/comments/<int:comment_id>/like/', views.comment_like_toggle_api, name='comment_like_toggle_api'),
    path('api/token/login/', CustomAuthToken.as_view(), name='api_token_login'),
    path('api/token/login/', obtain_auth_token, name='api_token_auth'),

]





