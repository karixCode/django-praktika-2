from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname= models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', blank=True, null=True)
    username = models.CharField(max_length=255, verbose_name='Логин', unique=True, blank=False)
    email = models.EmailField(max_length=255, verbose_name='Почта')
    password = models.CharField(max_length=255, verbose_name='Пароль', blank=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username