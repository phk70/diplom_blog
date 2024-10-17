from django.shortcuts import redirect, render, get_object_or_404

from django.urls import reverse_lazy
from django.utils import timezone
from .models import Post
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class PostListView(ListView):
    """Отображение всех постов с сортировкой по дате публикации"""

    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ['-published_date']


class PostDetailView(DetailView):
    """Отображение определенного поста по primary key"""

    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


@login_required
def post_add(request):
    if request.method == "POST":        
        title = request.POST.get('title')
        image = request.FILES["image"]
        text = request.POST.get('text')
        post = Post(author=request.user, title=title, image=image, text=text, published_date=timezone.now())
        post.save()
        return redirect('/', permanent=True)    
    return render(request, 'blog/post_add.html')


@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('/', permanent=True)      
    return render(request, "blog/post_delete.html", {'post': post})

class PostDeleteView(DeleteView):
    """Удаление определенного поста по primary key"""

    model = Post
    success_url = reverse_lazy('blog:post_list')


@login_required
def post_update(request, pk):
    
    post = Post.objects.get(pk=pk)
    if request.method == "POST":  
        post.author = request.user      
        post.title = request.POST.get('title')
        post.image = request.FILES.get("image", post.image)
        post.text = request.POST.get('text')  
        post.published_date = timezone.now()
        post.created_date = timezone.now()      
        post.save()
        return redirect('/', permanent=True)    
    return render(request, 'blog/post_update.html', {"post": post})


def posts_user(request, id):    
    return render(request, 'blog/posts_user.html', {'posts': Post.objects.filter(author=request.user.id)})


class Custom403View(TemplateView):
    """Отображение шаблона при недостатке прав доступа"""
    
    template_name = '403.html'
    status_code = 403

class Custom404View(TemplateView):
    """Отображение шаблона при отсутствии шаблона"""

    template_name = '404.html'
    status_code = 404