from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta: 
    	model = Post 
    	fields = ('title', 'familia', 'genero','especie', 'autor', 'texto', 'habito', 'vernacular', 'floracao', 'frutificacao', 'origem', 'mapa', 'referencias')