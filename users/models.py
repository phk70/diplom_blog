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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='_profile_images')
    city = models.CharField(max_length=30)   
    sex = models.CharField(max_length=7, choices=sexy, default=it)
    age = models.IntegerField()
    contact_number = models.CharField(max_length=50, default="+7..........")

    def __str__(self):
        return self.user.username

