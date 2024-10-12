from django.urls import path
from .views import post_list, post_detail, post_add, post_delete, post_update


urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post-add/', post_add, name='post_add'),
    path('post-delete/<int:pk>/', post_delete, name='post_delete'),
    path('post-update/<int:pk>/', post_update, name='post_update'),
]


