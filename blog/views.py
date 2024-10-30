from django.contrib import auth
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse

from django.urls import reverse_lazy
from django.utils import timezone
from blog.models import Post, Comment
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models import Q
from .forms import CommentForm
from django.template.loader import render_to_string


class PostListView(ListView):
    """Отображение всех постов с сортировкой по дате публикации"""

    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-published_date"]
    paginate_by = 3
    

def get_latest_comments(request):
    """Отображение 10 последних комментариев"""    
    
    latest_comments = Comment.objects.all().order_by('-created_date')[:10]
    html = render_to_string('blog/latest_comments.html', {'latest_comments': latest_comments})
    return HttpResponse(html)


class PostDetailView(DetailView):
    """Отображение определенного поста по primary key + отображение комментариев к постам"""    
    
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        if request.method == "POST":
            comment = Comment(
                post=post,
                author=request.user,
                text=request.POST.get("text")
            )
            comment.save()
        return redirect("blog:post_detail", pk=post.pk)


@login_required
def post_add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES["image"]
        text = request.POST.get("text")
        post = Post(
            author=request.user,
            title=title,
            image=image,
            text=text,
            published_date=timezone.now(),
        )
        post.save()
        return redirect("/", permanent=True)
    return render(request, "blog/post_add.html")


class PostDeleteView(DeleteView):
    """Удаление определенного поста по primary key"""

    model = Post
    success_url = reverse_lazy("blog:post_list")


@login_required
def post_update(request, pk):

    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.author = request.user
        post.title = request.POST.get("title")
        post.image = request.FILES.get("image", post.image)
        post.text = request.POST.get("text")
        post.published_date = timezone.now()
        post.created_date = timezone.now()
        post.save()
        return redirect("/", permanent=True)
    return render(request, "blog/post_update.html", {"post": post})


class SearchResultsView(ListView):
    """Поиск постов"""

    model = Post
    template_name = "blog/search.html"
    context_object_name = "posts"
    ordering = ["-published_date"]

    def get_queryset(self):
        query = self.request.GET.get("qsearch")
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )
        return posts


def posts_user(request, id):
    return render(
        request,
        "blog/posts_user.html",# 
        {"posts": Post.objects.filter(author=id)},
    )


@login_required
def comment_add(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("blog:post_detail", pk=post.pk)
    else:
        form = CommentForm()
    return render(request, "blog/comment_add.html", {"form": form})


class Custom403View(TemplateView):
    """Отображение шаблона при недостатке прав доступа"""

    template_name = "403.html"
    status_code = 403


class Custom404View(TemplateView):
    """Отображение шаблона при отсутствии шаблона"""

    template_name = "404.html"
    status_code = 404



