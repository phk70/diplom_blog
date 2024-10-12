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
    pass

def post_update(request, pk):
    pass

def add_product(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        measurement = request.POST.get("measurement")
        price = request.POST.get("price")
        photo = request.FILES["photo"]
        product = Products(title=title, description=description, measurement=measurement, price=price, photo=photo)
        product.save() 
        return redirect('/', permanent=True)       
    return render(request, "core/add_product.html")