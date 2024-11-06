from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def logout_view(request):
    return render(request, 'logout.html')


