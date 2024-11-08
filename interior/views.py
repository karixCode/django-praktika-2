from urllib.request import Request

from django.shortcuts import render, redirect

from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views import generic
from .models import User, Request
from django.shortcuts import render

def index(request):
    completed_requests = Request.objects.filter(status="completed").order_by('-timestamp')[:4]

    context = {
        'completed_requests': completed_requests,
    }

    return render(request, 'index.html', context)

class Register(generic.CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

def logout_view(request):
    logout(request)
    return redirect('index')

def profile(request):
    return render(request, 'interior/profile.html')

def user_requests(request, user_id):
    user = request.user
    requests = Request.objects.filter(user=user).order_by('-id')
    return render(request, 'interior/user_requests.html', {'requests': requests})

class Profile(generic.DetailView):
    model = User
    template_name = 'interior/profile.html'