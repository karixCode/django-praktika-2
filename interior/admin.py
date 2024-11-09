from django.contrib import admin
from .models import User, Category, Request

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Request)
