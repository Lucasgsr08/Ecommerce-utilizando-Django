# ecommerce/accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Adiciona um campo de email ao formulário de registro

    class Meta:
        model = User
        fields = ('username', 'email') # Define quais campos serão usados no formulário

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso. Por favor, escolha outro.")
        return email