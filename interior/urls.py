from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    # path('request/create/', views.RequestCreate.as_view(), name='request-create'),
    # path('request/<int:pk>/delete/', views.RequestDelete.as_view(), name='request-delete'),
]