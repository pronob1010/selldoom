from django.urls import path,include
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]