from django.shortcuts import render, redirect
from .models import Post

def mostrar_formulario(request):
    if request.method == 'POST':
        post = Post()
        post.titulo = request.POST.get('titulo')
        post.conteudo = request.POST.get('conteudo')
        post.autir = request.POST.get('autor')

        post.save()

        return redirect('/')

    return render(request, 'form.html')

def mostrar_home(request):
    posts = Post.objects.all()
    args = {
        'posts':posts
    }

    return render(request, 'index.html', args)
