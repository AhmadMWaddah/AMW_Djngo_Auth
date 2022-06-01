from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
]
