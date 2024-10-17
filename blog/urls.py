from django.urls import path
from .views import PostListView, PostDetailView, post_add, PostDeleteView, post_update, posts_user

app_name = "blog"

urlpatterns = [
    path('', PostListView. as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post-add/', post_add, name='post_add'),
    path('post-delete/<int:pk>/', PostDeleteView.as_view(), name='post_confirm_delete'),
    path('post-update/<int:pk>/', post_update, name='post_update'),
    path('posts-user/<int:id>/', posts_user, name='posts_user'),
]


