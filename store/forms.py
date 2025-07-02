# store/forms.py

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'text': 'Comentário',
            'rating': 'Avaliação (1 a 5)',
        }
