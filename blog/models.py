from django.db import models

from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    """Модель поста"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
