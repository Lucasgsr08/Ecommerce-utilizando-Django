# orders/forms.py

from django import forms
from .models import Order # Importa o modelo Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        # Defina os campos que você quer que o formulário colete do usuário.
        # Por exemplo, para criar um pedido, você precisaria dos dados do cliente.
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        # Você pode personalizar os widgets para melhor aparência no HTML, se necessário
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }