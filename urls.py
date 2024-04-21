from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signout/', views.singout, name='signout'),
    path('register/', views.Register_user, name='register')
]