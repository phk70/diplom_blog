from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Модель профиля пользователя. Расширение модели User"""

    male = "мужской"
    female = "женский"
    it = "..."
    sexy = (
        (male, "мужской"),
        (female, "женский"),
        (it, "...")        
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    image = models.ImageField(blank=True, upload_to='_profile_images', verbose_name="Фото")
    city = models.CharField(max_length=30, verbose_name="Город")   
    sex = models.CharField(max_length=7, choices=sexy, default=it, verbose_name="Пол")
    age = models.IntegerField(verbose_name="Возраст")
    contact_number = models.CharField(max_length=50, default="+7..........", verbose_name="Телефон")

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользоваьелей"


