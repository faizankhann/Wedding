from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('forget-password', views.password, name='forget-password'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),

]
