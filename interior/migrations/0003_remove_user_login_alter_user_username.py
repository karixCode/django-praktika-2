# Generated by Django 5.1.3 on 2024-11-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interior', '0002_alter_user_fio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='login',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True, verbose_name='Логин'),
        ),
    ]
