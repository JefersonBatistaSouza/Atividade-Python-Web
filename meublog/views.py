from django.shortcuts import render, get_object_or_404
from .models import Post, Comentario
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView

#Posts
class ListarPostsView(ListView):
    queryset = Post.publicados.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'meublog/post/listarposts.html'


class DetalharPostView(DetailView):
    model = Post
    template_name = 'meublog/post/detalharpost.html'
    id = None
    
    def get_context_data(self, **kwargs):
        #Pega o contexto da página
        context = super(DetailView, self).get_context_data(**kwargs)
        context['comentarios'] = Comentario.ativosG.filter(fk_post=kwargs.get('object').id)
        return context
    
    
'''
def listar_posts(request):
    posts = Post.publicados.all() #Este é o gerenciador criado
    return render(request, 'meublog/post/listarposts.html', {'posts': posts})

def detalhar_post(request, ano, mes, dia, slug, pk):
    post = get_object_or_404(Post, slug=slug, status='publicado', publicado__year=ano, publicado__month=mes, publicado__day=dia)
    comentarios = Comentario.ativosG.filter(ativo=True, fk_post=pk)
    return render(request, 'meublog/post/detalharpost.html', {'post': post, 'comentarios': comentarios})
'''