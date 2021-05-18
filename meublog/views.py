from django.shortcuts import render, get_object_or_404
from .models import Post, Comentario

#Posts
def listar_posts(request):
    posts = Post.publicados.all() #Este é o gerenciador criado
    return render(request, 'meublog/post/listarposts.html', {'posts': posts})

def detalhar_post(request, ano, mes, dia, slug):
    post = get_object_or_404(Post, slug=slug, status='publicado', publicado__year=ano, publicado__month=mes, publicado__day=dia)
    return render(request, 'meublog/post/detalharpost.html', {'post': post})

#Comentarios
def listar_comentarios(request):
    comentarios = Comentario.ativosG.all()
    return render(request, 'meublog/comentarios/listarcomentarios.html', {'comentarios': comentarios})


