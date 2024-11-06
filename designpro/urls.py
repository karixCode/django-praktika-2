from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/interior/', permanent=True)),
    path('admin/', admin.site.urls),
    path('interior/', include('interior.urls')),
]