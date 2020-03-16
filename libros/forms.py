from django import forms
from .models import Libro
from django.db import IntegrityError

class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['title', 'author', 'content', 'image', 'user', 'categories', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Autor'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'categories': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Categorías'}),
            'status': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Status'}),
        }
        labels = {
            'title':'', 'author':'', 'categories':'', 'content': '', 'status': '', 'user': 'Publicado por'
        }