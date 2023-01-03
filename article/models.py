from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(blank=True, max_length=1000, verbose_name='Контент')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория доступа')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(default=None, max_length=55)

    def __str__(self):
        return self.title
