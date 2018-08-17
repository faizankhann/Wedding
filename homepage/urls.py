from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('/help1/', views.help1, name="help1"),
    path('/guest/', views.guest, name="guest"),
    path('/checklist/', views.checklist, name="checklist"),
    path('/budget/', views.budget, name="budget")

]
