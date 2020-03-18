from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Titulo'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Orden'}),
        }
        
        labels = {
            'title':'Titulo', 'order':'Orden', 'content':'Contenido'
        }
        
