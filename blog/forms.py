from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """Форма для создания комментария"""    
    class Meta:
        model = Comment
        fields = ('text',)


class PostForm(forms.ModelForm):
    """Форма для создания поста"""
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')