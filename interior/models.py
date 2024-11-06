from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    username = models.CharField(max_length=255, verbose_name='Логин', unique=True, blank=False)
    email = models.EmailField(max_length=255, verbose_name='Почта')
    password = models.CharField(max_length=255, verbose_name='Пароль', blank=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username