from django import forms
from .models import Post

class Posts(form.ModelForm):
    class Postagem:
        model = Post
        fields = [
            'titulo',
            'conteudo',
            'autor'
        ]