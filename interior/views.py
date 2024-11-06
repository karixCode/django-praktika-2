from django.shortcuts import render, redirect

from .forms import RegisterForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout

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
