# store/apps.py

from django.apps import AppConfig

class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store' # <-- ISSO É O MAIS IMPORTANTE AQUI! Deve ser 'store'