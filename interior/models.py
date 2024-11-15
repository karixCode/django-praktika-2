from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname= models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', blank=True, null=True)
    username = models.CharField(max_length=255, verbose_name='Логин', unique=True)
    email = models.EmailField(max_length=255, verbose_name='Почта')
    password = models.CharField(max_length=255, verbose_name='Пароль')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Категория')

    def __str__(self):
        return self.name

class Request(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, help_text='Выберите категорию')
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def validate_image(image):
        valid_mime_types = ['image/jpeg', 'image/png', 'image/bmp']
        mime_type = image.file.content_type
        if mime_type not in valid_mime_types:
            raise ValidationError("Формат файла должен быть: jpg, jpeg, png, bmp.")

        file_size = image.size
        limit_mb = 2
        if file_size > limit_mb * 1024 * 1024:
            raise ValidationError("Размер файла не должен превышать 2 МБ.")

    design_image = models.ImageField(upload_to='interior/design',validators=[validate_image], verbose_name='Фото')

    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('in_progress', 'Принято в работу'),
        ('completed', 'Выполнено'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return self.title