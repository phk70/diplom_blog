from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    post_add, 
    PostDeleteView, 
    post_update, 
    posts_user, 
    SearchResultsView, 
    comment_add,
    get_latest_comments
)


app_name = "blog"

urlpatterns = [
    path('', PostListView. as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post-add/', post_add, name='post_add'),
    path('post-delete/<int:pk>/', PostDeleteView.as_view(), name='post_confirm_delete'),
    path('post-update/<int:pk>/', post_update, name='post_update'),
    path('posts-user/<int:id>/', posts_user, name='posts_user'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('get-latest-comments/', get_latest_comments, name='get_latest_comments'),   
]

handler404 = 'blog.views.Custom404View.as_view()'
handler403 = 'blog.views.Custom403View.as_view()'
