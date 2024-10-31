from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post
from .telegram_bot import send_telegram_message
from datetime import datetime

@receiver(post_save, sender=Post)
def new_post_signal(sender, instance, created, **kwargs):
    if created:
        message = f"""
Cоздан новый пост {instance.pk}-{instance.title}: 
Автор: {instance.author}"""
        send_telegram_message(message)
    
    else:
        message = f"""
Обновлен пост {instance.pk}-{instance.title}: 
Автор: {instance.author}"""
        send_telegram_message(message)


@receiver(post_delete, sender=Post)
def notify_about_post_delete(sender, instance, **kwargs):
    message = f"""
Удален пост {instance.pk}-{instance.title} от {instance.published_date.strftime('%Y-%m-%d')}:
Автор: {instance.author}"""
    send_telegram_message(message)