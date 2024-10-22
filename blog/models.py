from tabnanny import verbose
from django.db import models

from django.conf import settings
from django.utils import timezone




class Post(models.Model):
    """Модель поста"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст поста')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='blog/image/', blank=True, null=True, verbose_name='Изображение')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Comment(models.Model):
    """Модель комментария"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Запись')
    author = models.CharField(max_length=200, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст комментария')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    approved_comment = models.BooleanField(default=False, verbose_name='Согласован')

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
