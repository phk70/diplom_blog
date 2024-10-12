from cgitb import text
from turtle import title
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post


def post_list(request):
    # posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_add(request):
    if request.method == "POST":        
        title = request.POST.get('title')
        image = request.FILES["image"]
        text = request.POST.get('text')
        post = Post(author=request.user, title=title, image=image, text=text, published_date=timezone.now())
        post.save()
        return redirect('/', permanent=True)    
    return render(request, 'blog/post_add.html')

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('/', permanent=True)      
    return render(request, "blog/post_delete.html", {'post': post})

def post_update(request, pk):
    pass
