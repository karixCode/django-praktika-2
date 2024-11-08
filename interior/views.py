from urllib.request import Request

from django.shortcuts import render, redirect

from .forms import RegisterForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.

def index(request):
    return render(request, 'index.html')

class Register(generic.CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

def logout_view(request):
    logout(request)
    return redirect('index')

def profile(request):
    return render(request, 'interior/profile.html')

class AuthorCreate(CreateView):
    model = Request
    fields = ['title', 'description', 'category', 'design_image']

class AuthorDelete(DeleteView):
    model = Request
    success_url = reverse_lazy('profile')