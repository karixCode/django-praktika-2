from django.contrib import admin
from .models import User, Category, Request
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Request)
